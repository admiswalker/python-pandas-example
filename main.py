import io
import pandas as pd
import numpy as np

def main():
    print('hello')

    df_data = pd.DataFrame([[111, 'aaa', 100, 123, 987],
                            [222, 'bbb', 200, 321, 777]],
                           columns=['user_id', 'user_name', 'param_1', 'param_2', 'param_3'])
    print(df_data)
    print()

    l_col = ['param_1', 'param_2', 'param_3']
    l_is_sig = ['>=', '>=', '>=']
    l_val = [150, 150, 150]

    df_data[l_col[0]+'_TF'] = np.where(df_data[l_col[0]] > l_val[0], 1, 0)
    print(df_data)
    print()

    #df_data[l_col[0]+'_TF'] = eval(f"np.where(df_data[l_col[0]] {l_is_sig[0]} l_val[0], 1, 0)")
    #print(df_data)
    #print()

    for i in range(len(l_col)):
        df_data[l_col[i]+'_TF'] = eval(f"np.where(df_data[l_col[i]] {l_is_sig[i]} l_val[i], 1, 0)")
    print(df_data)
    print()

    # sum
    #df_data['TF_sum'] = df_data[l_col[0]+'_TF'] + df_data[l_col[1]+'_TF'] + df_data[l_col[2]+'_TF']
    #print(df_data)
    #print()
    
    # sum
    df_data['TF_sum'] = int(0)
    for i in range(len(l_col)):
        df_data['TF_sum'] += df_data[l_col[i]+'_TF']
    print(df_data)
    print()
    
    
main()
