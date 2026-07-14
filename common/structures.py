import numpy as np

class Sorn(object):
    def __init__(self, N_e, N_i, T_e_max, T_i_max, eta_STDP, eta_inh, mu_IP, p_SP, eta_SP, sig_sq_ip):
        
        ## general parameters
        self.N_e = N_e ## number of e neurons
        self.N_i = N_i ## number of i neurons
        
        ## plasticity parameters
        self.eta_STDP = eta_STDP 
        self.eta_inh = eta_inh
        self.mu_IP = mu_IP
        self.p_SP = p_SP
        self.eta_SP = eta_SP
        self.sig_sq_ip = sig_sq_ip

    ## Build W_ee
        raw_ee = np.random.uniform(0, 0.1, size=(N_e, N_e)) ## Random weights drawn from uniform distribution between 0 and 0.1
        tf_ee = np.random.rand(self.N_e, self.N_e) < 0.1 ## T/F grid to overlay on raw_ee; cuts down on 90% of weights with 10% "True" values when added as a mask to W_ee|| not needed later --> not a self. arg
        np.fill_diagonal(tf_ee, False) ## Removes self connections

        guar_row_connection = tf_ee.any(axis=1) ## guarantees each row has at least 1 True value
        empty_rows = np.where(guar_row_connection == False)[0] ## finds rows that are empty
        for i in empty_rows:
            while True: ## as long as there are empty rows...
                new_row = np.random.rand(self.N_e) < 0.1 ## recreate a new row with 10% True values
                new_row[i] = False ## removes self connection at position i from that new row
                if new_row.any(): ## if the new row has at least 1 True value...
                    tf_ee[i] = new_row ## replace empty row with this new row
                    break
       
        self.W_ee = raw_ee * tf_ee ## Compile full matrix now that tf_ee is ensured to have no empty rows
        self.W_ee = self.W_ee / self.W_ee.sum(axis=1, keepdims=True) ## Normalization for each row's connections to sum to 1: for each connection in W_ee, divide them by the sum of each row --> .sum(axis=1); keepdims=True ensures sum is a column vector for division to work
        
        self.R_ee = self.W_ee > 0.0 ## record which connections/cells of W_ee are non-zero 

    ## Build W_ei
        raw_ei = np.random.uniform(0, 0.1, size=(N_e, N_i)) ## Random weights drawn from uniform distribution between 0 and 0.1
        tf_ei = np.random.rand(self.N_e, self.N_i) < 0.2 ## T/F grid to overlay on raw_ei; cuts down on 80% of weights when added as a mask to W_ei
        
        empty_rows = np.where(tf_ei.sum(axis=1) == 0)[0] ## finds rows that are empty
        for i in empty_rows:
            while True: ## as long as there are empty rows...
                new_row = np.random.rand(self.N_i) < 0.2 ## recreate a new row with 20% True values
                if new_row.any(): ## if the new row has at least 1 True value...
                    tf_ei[i] = new_row ## replace empty row with this new row
                    break
        
        self.W_ei = raw_ei * tf_ei ## Compile full matrix now that tf_ei is ensured to have no empty rows
        self.W_ei = self.W_ei / self.W_ei.sum(axis=1, keepdims=True) ## Normalization of weights; each row adds to 1
        
        self.R_ei = self.W_ei > 0.0

    ##build W_ie
        raw_ie = np.random.uniform(0, 0.1, size=(N_i, N_e)) ## Random weights drawn from uniform distribution between 0 and 0.1
        tf_ie = np.random.rand(N_i, N_e) < 1.0
        self.W_ie = raw_ie * tf_ie ## Compile full matrix
        self.W_ie = self.W_ie / self.W_ie.sum(axis=1, keepdims=True) ## Normalization
        ## no mask needed; no plasticity applied to this matrix

    ##build T_e & T_i
        self.T_e = np.random.uniform(0, T_e_max, size=(N_e)) ## each neuron gets own threshold drawn from uniform distribution over the interval [0 and T_e_max]
        self.T_i = np.random.uniform(0, T_i_max, size=(N_i)) ## each neuron gets own threshold drawn from uniform distribution over the interval [0 and T_i_max]

    ## build x & y (based on source code, not the paper)
        self.x = (np.random.rand(N_e) < mu_IP).astype(int) ## each neuron has a 10% chance of being active at initialization
        self.y = np.zeros(N_i, dtype=int) ## all inhibitory neurons start inactive

    ## define H_ip formula
        if sig_sq_ip > 0:
            self.H_ip = np.random.normal(mu_IP, np.sqrt(sig_sq_ip), size=(N_e)) ## each neuron gets its own target firing rate drawn from a normal distribution with mean mu_IP and standard deviation sqrt(sig_sq_ip)
        else:
            self.H_ip = np.full(N_e, mu_IP) ## all neurons have the same target firing rate of mu_IP; makes an array full of just the value of mu_IP
        
    ## define U_ext
        self.U_ext = np.zeros(N_e) ## initialize U_ext as a zero vector of length N_e; baseline case is no external drive
            

    def STDP(self):
        pass

    def iSTDP(self):
        pass

    def SP(self):
        pass

    def IP(self):
        pass
