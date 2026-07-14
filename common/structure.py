class Sorn(object):
    def __init__(self, N_e, N_i, W_ee, W_ei, W_ie, x, y, xi_E, xi_I, Uext, W_eu, T_e, T_i, T_e_max, T_i_max, eta_STDP, eta_inh, mu_IP, p_SP, eta_SP, H_ip, sig_sq_ip):
        self.N_e = N_e
        self.N_i = N_i
        self.W_ee = W_ee
        self.W_ei = W_ei
        self.W_ie = W_ie
        self.x = x
        self.y = y
        self.xi_E = xi_E
        self.xi_I = xi_I
        self.Uext = Uext
        self.W_eu = W_eu
        self.T_e = T_e
        self.T_i = T_i
        self.T_e_max = T_e_max
        self.T_i_max = T_i_max
        self.eta_STDP = eta_STDP
        self.eta_inh = eta_inh
        self.mu_IP = mu_IP
        self.p_SP = p_SP
        self.eta_SP = eta_SP
        self.H_ip = H_ip
        self.sig_sq_ip = sig_sq_ip

    def STDP(self):
        pass

    def iSTDP(self):
        pass

    def SP(self):
        pass

    def IP(self):
        pass
