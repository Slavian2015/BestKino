import pandas as pd
import numpy as np

import os



# ##################################   SHOW ALL ROWS & COLS   ####################################
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.expand_frame_repr', False)
# # pd.set_option('max_colwidth', -1)


main_path_data = os.path.abspath("./data")

def refresh_BD():

    #################################   CREAT NEW FILES   ##########################################

    if os.path.isfile(main_path_data + "\\server.csv"):
        pass
    else:
        dtt = ['match_id', 'Mlinks', 'T1names', 'T2names', 'T1logos',
              'T2logos', 'Mtime', 'Mdate', 'Mtour', 'Mtypes']
        dftt = pd.DataFrame(columns=dtt)
        dftt.to_csv(main_path_data + "\\server.csv", index=False, header=True)
        pass

    if os.path.isfile(main_path_data + "\\all_cards.csv"):
        pass
    else:
        column_names = [
            'Mid',
            'T1name',
            'T2name',
            'T1logo',
            'T2logo',

            'Mstatus',
            'T1score',
            'T2score',

            'Mdate',
            'Mtime',
            'Mtour',
            'Mtypes',

            'WR',
            'FB',
            'F10',

            'WR2',
            'FB2',
            'F102',

            'P11',
            'P12',
            'P13',
            'P14',
            'P15',

            'P21',
            'P22',
            'P23',
            'P24',
            'P25',
            'P11_photo',
            'P12_photo',
            'P13_photo',
            'P14_photo',
            'P15_photo',
            'P21_photo',
            'P22_photo',
            'P23_photo',
            'P24_photo',
            'P25_photo',
            'P11_score',
            'P12_score',
            'P13_score',
            'P14_score',
            'P15_score',
            'P21_score',
            'P22_score',
            'P23_score',
            'P24_score',
            'P25_score',

        ]
        df = pd.DataFrame(columns=column_names)
        df.to_csv(main_path_data + "\\all_cards.csv", index=False, header=True)
        pass

    if os.path.isfile(main_path_data + "\\all_h2h.csv"):
        pass
    else:
        dwh2h = [
            'Mid',
            'H2H_date',
            'H2H_time',
            'H2H_total_t1',
            'H2H_total_t2',
            ]

        dfh2h = pd.DataFrame(columns=dwh2h)
        dfh2h.to_csv(main_path_data + "\\all_h2h.csv", index=False, header=True)
        pass

    if os.path.isfile(main_path_data + "\\all_t1.csv"):
        pass
    else:
        dwt1 = [
            'Mid',
            'T1_last_date',
            'T1_last_time',
            'T1_last_name',
            'T1_last_logo',
            'T1_last_total_main',
            'T1_last_total_vs',
            ]

        dft1 = pd.DataFrame(columns=dwt1)
        dft1.to_csv(main_path_data + "\\all_t1.csv", index=False, header=True)
        pass

    if os.path.isfile(main_path_data + "\\all_t2.csv"):
        pass
    else:
        dwt2 = [
            'Mid',
            'T2_last_date',
            'T2_last_time',
            'T2_last_name',
            'T2_last_logo',
            'T2_last_total_main',
            'T2_last_total_vs',
        ]

        dft2 = pd.DataFrame(columns=dwt2)
        dft2.to_csv(main_path_data + "\\all_t2.csv", index=False, header=True)
        pass

    # if os.path.isfile(main_path_data + "\\all_test.csv"):
    #     pass
    # else:
    #     dwttest = [
    #         'Mid',
    #         'T2_last_date',
    #         'T2_last_time',
    #         'T2_last_name',
    #         'T2_last_logo',
    #         'T2_last_total_main',
    #         'T2_last_total_vs',
    #     ]
    #
    #     dfttt = pd.DataFrame(columns=dwttest)
    #     dfttt.to_csv(main_path_data + "\\all_test.csv", index=False, header=True)
    #     pass





    refreshBD = pd.read_csv(main_path_data + "\\refresh.csv")
    serverBD = pd.read_csv(main_path_data + "\\server.csv")
    all_cardsBD = pd.read_csv(main_path_data + "\\all_cards.csv")
    all_h2hBD = pd.read_csv(main_path_data + "\\all_h2h.csv")
    all_t1BD = pd.read_csv(main_path_data + "\\all_t1.csv")
    all_t2BD = pd.read_csv(main_path_data + "\\all_t2.csv")



    #######################   BD CHANGES   #####################################

    df_new_items = refreshBD.loc[~refreshBD['match_id'].isin(serverBD['match_id'])]
    df_old_items = serverBD.loc[~serverBD['match_id'].isin(refreshBD['match_id'])]

    if df_old_items.shape[0] > 0:
        serverBD = serverBD.set_index("match_id")
        serverBD = serverBD.drop(df_old_items['match_id'], axis=0)
        serverBD = serverBD.reset_index()
        serverBD.to_csv(main_path_data + "\\server.csv", index=False, header=False)
    else:
        pass

    #############   Create Mcard and add to All_Cards  ##########################

    if df_new_items.shape[0] > 0:


        for i in df_new_items['Mlinks']:
            dt = df_new_items[(df_new_items['Mlinks'].isin([i]))]

            result = Card_parser.newCard(i, dt.iloc[0]['match_id'])

            all_cardsBD = all_cardsBD.append(result[0], ignore_index=True, sort=False)
            all_h2hBD = all_h2hBD.append(result[1], ignore_index=True, sort=False)
            all_t1BD = all_t1BD.append(result[2], ignore_index=True, sort=False)
            all_t2BD = all_t2BD.append(result[3], ignore_index=True, sort=False)

        all_cardsBD.to_csv(main_path_data + "\\all_cards.csv", index=False, header=True)
        all_h2hBD.to_csv(main_path_data + "\\all_h2h.csv", index=False, header=True)
        all_t1BD.to_csv(main_path_data + "\\all_t1.csv", index=False, header=True)
        all_t2BD.to_csv(main_path_data + "\\all_t2.csv", index=False, header=True)
        serverBD = serverBD.append(df_new_items)
        serverBD.to_csv(main_path_data + "\\server.csv", index=False, header=True)


    else:
        pass