from scipy.stats import norm


chat_id = 294776608

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x_conv_rate = x_success / x_cnt
    y_conv_rate = y_success / y_cnt
    
    std_error = np.sqrt(x_conv_rate * (1 - x_conv_rate) / x_cnt + y_conv_rate * (1 - y_conv_rate) / y_cnt)
    
    z_score = (y_conv_rate - x_conv_rate) / std_error
    
    alpha = 0.03
    critical_value = norm.ppf(1 - alpha / 2)
    
    return z_score > critical_value
