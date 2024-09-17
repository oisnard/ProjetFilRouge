import pandas as pd
import lib_fileinput as lib_input
import lib_text as lib_text


y_train = lib_input.get_ytrain()
X_train = lib_input.get_xtrain()


df_train = X_train
print("Text cleaning")
df_train['description'] = df_train['description'].fillna("")
Full_Descr = df_train['designation'].astype(str) + ' ' + df_train['description'].astype(str)
df_train['tokens'] = Full_Descr.apply(lib_text.text_to_tokens)
df_train['nb_token'] = df_train['tokens'].apply(len)

print("Store tokens")
df_train.to_csv('..\\Data\\X_train_design_tokens.csv')


df = pd.concat([df_train, y_train], axis=1)

print("Build list of overall tokens...")
unified_list_tokens = []



for lists in df['tokens']:
    for token in lists:
        if token not in unified_list_tokens:
            unified_list_tokens.append(token)

print(len(unified_list_tokens))


print("Build Pivot table for tokens...")
df_token = pd.DataFrame(index=unified_list_tokens, columns=df['prdtypecode'].unique())

df_token = df_token.fillna(0)
print(df_token.shape)

#print(df)
list_cat_id = df['prdtypecode'].unique()
print(list_cat_id)
for cat_id in list_cat_id:
    print("prdtypecode = ", cat_id)
    df_tmp = df.loc[df['prdtypecode']==cat_id]
    for list_tokens in df_tmp['tokens']:
        for token in list_tokens:
            df_token.at[token,cat_id] = df_token.at[token,cat_id] + 1

print('Store token pivot table')
df_token.to_csv('..\\Data\\train_tokens.csv')


