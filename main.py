import io
import pandas as pd
import numpy as np

def main01_a():
    print('main01_a')

    df_data = pd.DataFrame([[111, 'aaa', 100, 123, 987],
                            [222, 'bbb', 200, 321, 777]],
                           columns=['user_id', 'user_name', 'param_1', 'param_2', 'param_3'])
    print(df_data)
    print()

    l_col = ['param_1', 'param_2', 'param_3']
    l_is_sig = ['>=', '>=', '>=']
    l_val = [150, 150, 150]
    
    df_res = df_data[df_data[l_col[0]] >= l_val[0]]
    print(df_res)
    print()
    
    df_res = eval(f"df_data[df_data[l_col[0]] {l_is_sig[0]} l_val[0]]")
    print(df_res)
    print()

    # 指定した列だけ取得する
    df_res = df_res.loc[:,['user_id','user_name', l_col[0]]]
    print(df_res)
    print()

    # 列名を変更する
    df_res = df_res.rename(columns={l_col[0]:'val'})
    df_res['param_name'] = l_col[0]
    print(df_res)
    print()

    """
    df_test = pd.DataFrame([[111, 'aaa', 'param_1', 100],
                            [111, 'aaa', 'param_2', 123],
                            [111, 'aaa', 'param_3', 987],
                            [222, 'bbb', 'param_1', 200],
                            [222, 'bbb', 'param_2', 321],
                            [222, 'bbb', 'param_3', 777]],
                           columns=['user_id', 'user_name', 'param_name', 'value'])
    print(df_test)
    print()
    """

def main01_b():
    print('main01_b')

    df_data = pd.DataFrame([[111, 'aaa', 100, 123, 987],
                            [222, 'bbb', 200, 321, 777]],
                           columns=['user_id', 'user_name', 'param_1', 'param_2', 'param_3'])
    print(df_data)
    print()

    l_col = ['param_1', 'param_2', 'param_3']
    l_is_sig = ['>=', '>=', '>=']
    l_val = [150, 150, 150]
    
    df_res = pd.DataFrame()
    for i in range(len(l_col)):
        df_tmp = eval(f"df_data[df_data[l_col[i]] {l_is_sig[i]} l_val[i]]")
        df_tmp = df_tmp.loc[:,['user_id','user_name', l_col[i]]] # 指定した列だけ取得する
        df_tmp = df_tmp.rename(columns={l_col[i]:'val'}) # 列名を変更する
        df_tmp['param_name'] = l_col[i] # 列を追加する
        df_tmp['cond1'] = 'T' # 列を追加する
        print(df_tmp)
        print()
        df_res = pd.concat([df_res, df_tmp])
    
    print(df_res)
    print()

def main02():
    print('main02')
    # diff from prev

def main03_a():
    print('main03_a')

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
    
def main03_b():
    print('main03_b')
    
    sum_threshold = 2
    
    df_data = pd.DataFrame([[111, 'aaa', 100, 123, 987],
                            [222, 'bbb', 200, 321, 777]],
                           columns=['user_id', 'user_name', 'param_1', 'param_2', 'param_3'])
    print(df_data)
    print()

    l_col = ['param_1', 'param_2', 'param_3']
    l_is_sig = ['>=', '>=', '>=']
    l_val = [150, 150, 150]

    # sum
    #df_data['TF_sum'] = int(0)
    #for i in range(len(l_col)):
    #    df_data['TF_sum'] += np.where(df_data[l_col[i]] >= l_val[i], 1, 0)
    #print(df_data)
    #print()

    # sum
    df_data['TF_sum'] = int(0)
    for i in range(len(l_col)):
        df_data['TF_sum'] += eval(f"np.where(df_data[l_col[i]] {l_is_sig[i]} l_val[i], 1, 0)")
    print(df_data)
    print()
    
    # ex: np.where's return value:
    print(np.where(df_data[l_col[i]] >= l_val[i], 1, 0))

    # sum
    df_data['over_threshold'] = np.where(df_data['TF_sum'] >= sum_threshold, True, False)
    print(df_data)
    print()

#main01_a()
main01_b()
#main02()
#main03_a()
#main03_b()

