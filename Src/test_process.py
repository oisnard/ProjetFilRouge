import pandas as pd
import lib_fileinput as lib_input
import lib_text as lib_text


X_test = lib_input.get_xtest()


df_test = X_test
print("Text cleaning")
df_test['description'] = df_test['description'].fillna("")
Full_Descr = df_test['designation'].astype(str) + ' ' + df_test['description'].astype(str)
df_test['tokens'] = Full_Descr.apply(lib_text.text_to_tokens)
df_test['nb_token'] = df_test['tokens'].apply(len)

print("Store tokens")
df_test.to_csv('..\\Data\\X_test_design_tokens.csv')


#df = pd.concat([df_train, y_train], axis=1)

print("Build list of overall tokens...")
unified_list_tokens = []



for lists in df_test['tokens']:
    for token in lists:
        if token not in unified_list_tokens:
            unified_list_tokens.append(token)

print(len(unified_list_tokens))


df_token = pd.Series(index=unified_list_tokens)
df_token = df_token.fillna(0)
df_token = df_token.astype(int)

for list_tokens in df_test['tokens']:
    for token in list_tokens:
        df_token[token] = df_token[token]+1

df_token.to_csv('..\\Data\\test_tokens.csv')

