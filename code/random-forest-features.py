def predict_typeoftransaction(data={}):
    """ Predictor for TypeOfTransaction from model/53a5c562c8db6379900016c4
        Predictive model by BigML - Machine Learning Made Easy
    """
    if (not 'srv_count_' in data or data['srv_count_'] is None):
        return u'normal.'
    if (data['srv_count_'] > 64):
        return u'smurf.'
    if (data['srv_count_'] <= 64):
        if (not 'flag_' in data or data['flag_'] is None):
            return u'normal.'
        if (data['flag_'] == 'SF'):
            if (not 'protocol_type_' in data or data['protocol_type_'] is None):
                return u'normal.'
            if (data['protocol_type_'] == 'icmp'):
                if (not 'dst_host_count_' in data or data['dst_host_count_'] is None):
                    return u'normal.'
                if (data['dst_host_count_'] > 121):
                    return u'smurf.'
                if (data['dst_host_count_'] <= 121):
                    return u'normal.'
            if (data['protocol_type_'] != 'icmp'):
                if (not 'root_shell_' in data or data['root_shell_'] is None):
                    return u'normal.'
                if (data['root_shell_'] == '0'):
                    if (not 'dst_host_srv_count_' in data or data['dst_host_srv_count_'] is None):
                        return u'normal.'
                    if (data['dst_host_srv_count_'] > 91):
                        return u'normal.'
                    if (data['dst_host_srv_count_'] <= 91):
                        if (not 'dst_host_count_' in data or data['dst_host_count_'] is None):
                            return u'normal.'
                        if (data['dst_host_count_'] > 3):
                            if (not 'dst_host_serror_rate_' in data or data['dst_host_serror_rate_'] is None):
                                return u'normal.'
                            if (data['dst_host_serror_rate_'] > 0.035):
                                if (not 'dst_host_diff_srv_rate_' in data or data['dst_host_diff_srv_rate_'] is None):
                                    return u'normal.'
                                if (data['dst_host_diff_srv_rate_'] > 0.035):
                                    return u'normal.'
                                if (data['dst_host_diff_srv_rate_'] <= 0.035):
                                    if (not 'dst_host_same_src_port_rate_' in data or data['dst_host_same_src_port_rate_'] is None):
                                        return u'spy.'
                                    if (data['dst_host_same_src_port_rate_'] > 0.01):
                                        return u'guess_passwd.'
                                    if (data['dst_host_same_src_port_rate_'] <= 0.01):
                                        return u'spy.'
                            if (data['dst_host_serror_rate_'] <= 0.035):
                                if (not 'serror_rate_' in data or data['serror_rate_'] is None):
                                    return u'normal.'
                                if (data['serror_rate_'] > 0.495):
                                    return u'buffer_overflow.'
                                if (data['serror_rate_'] <= 0.495):
                                    return u'normal.'
                        if (data['dst_host_count_'] <= 3):
                            if (not 'dst_host_srv_diff_host_rate_' in data or data['dst_host_srv_diff_host_rate_'] is None):
                                return u'normal.'
                            if (data['dst_host_srv_diff_host_rate_'] > 0.025):
                                if (not 'num_failed_logins_' in data or data['num_failed_logins_'] is None):
                                    return u'normal.'
                                if (data['num_failed_logins_'] == '0'):
                                    return u'normal.'
                                if (data['num_failed_logins_'] != '0'):
                                    return u'guess_passwd.'
                            if (data['dst_host_srv_diff_host_rate_'] <= 0.025):
                                if (not 'src_bytes_' in data or data['src_bytes_'] is None):
                                    return u'normal.'
                                if (data['src_bytes_'] > 4):
                                    if (not 'num_file_creations_' in data or data['num_file_creations_'] is None):
                                        return u'normal.'
                                    if (data['num_file_creations_'] == '0'):
                                        return u'normal.'
                                    if (data['num_file_creations_'] != '0'):
                                        return u'buffer_overflow.'
                                if (data['src_bytes_'] <= 4):
                                    return u'buffer_overflow.'
                if (data['root_shell_'] != '0'):
                    if (not 'dst_host_same_src_port_rate_' in data or data['dst_host_same_src_port_rate_'] is None):
                        return u'buffer_overflow.'
                    if (data['dst_host_same_src_port_rate_'] > 0.09):
                        return u'buffer_overflow.'
                    if (data['dst_host_same_src_port_rate_'] <= 0.09):
                        return u'normal.'
        if (data['flag_'] != 'SF'):
            if (not 'src_bytes_' in data or data['src_bytes_'] is None):
                return u'portsweep.'
            if (data['src_bytes_'] > 63):
                if (data['src_bytes_'] > 135):
                    if (not 'dst_host_srv_rerror_rate_' in data or data['dst_host_srv_rerror_rate_'] is None):
                        return u'normal.'
                    if (data['dst_host_srv_rerror_rate_'] > 0.085):
                        if (not 'logged_in_' in data or data['logged_in_'] is None):
                            return u'buffer_overflow.'
                        if (data['logged_in_'] == '1'):
                            return u'buffer_overflow.'
                        if (data['logged_in_'] != '1'):
                            return u'portsweep.'
                    if (data['dst_host_srv_rerror_rate_'] <= 0.085):
                        return u'normal.'
                if (data['src_bytes_'] <= 135):
                    return u'guess_passwd.'
            if (data['src_bytes_'] <= 63):
                return u'portsweep.'