#importing Libraries
import gspread

#defining Function
def sheets_automate():
    #credentials there is an api to access it in google developer console 
    acc = gspread.service_account('D:\\git_files\\Python-Codes-1\\all_codes\\new_id.json')

    #Openning ALL FILES

    first_sheet = acc.open('candidates')
    second_sheets = acc.open('rough')   
    all_data_merge = acc.open('samplesheet')

    #accessing sheets
    fs_s1 = first_sheet.worksheet('Sheet1')
    ss_s1 = second_sheets.worksheet('Sheet1')
    adm_s1 = all_data_merge.worksheet('Sheet1')



    #getting name coloumns for rough sheet -> getting data type is list
    uniqueid_ss_s1 = ss_s1.col_values(2)

    '''
    Creating a loop in which every name got fetched and then it will fecth all uniqueid and 
    going to check into candidates sheet and if available then fetch all data from candidates
    sheet and paste into sample sheet
    '''

    for i in uniqueid_ss_s1:
        #finding data into candidates
        location_candidates = fs_s1.find(i)
        location_candidates = str(location_candidates)

        #extracting Row value 
        lst = location_candidates.split(' ')
        if len(lst)>1:
            row_coloms = lst[1]
            row_value = 0
            col_value = 0
            #for rows
            for i in row_coloms:
                if i.isdigit():
                    i = int(i)
                    row_value = (row_value*10)+i
                elif i =='C':
                    break
            #for columns
            # for i in row_coloms:
            #     if i.isdigit():
            
                    
            #fetching data from candidates and rough
            row_data = fs_s1.row_values(row_value)

            #appending data to sample sheet
            adm_s1.append_row(row_data)

            #test1->adding sample comment result:->failed
            # adm_s1.insert_cols(pranav_choice_ss_s1_cno_6)

            #test2 ->adding again sample data result:->failed
            # for i in pranav_choice_ss_s1_cno_6:
            #     acell_no_variable = 2
            #     adm_s1.acell(f'F{acell_no_variable}',i)

            #test3 ->adding again sample data result:-> failed
            # for i in pranav_choice_ss_s1_cno_6:
            #     acell_no_variable = 2
            #     adm_s1.update_acell(f'F{acell_no_variable}',i)
            #     acell_no_variable+=1

            #test4 ->adding again sample data result:-> failed
            # for i in pranav_choice_ss_s1_cno_6:
            #     print(i)

            #test5 -> repetion of test3 ->adding again sample data result:-> Failed
            # for i in pranav_choice_ss_s1_cno_6:
            #     acell_no_variable = 2
            #     adm_s1.update_acell(f'W{acell_no_variable}',i)
            #     acell_no_variable+=1

            #test6 -> repetion of test4 with for loop remove and minor changes result:-> sucessfull for 1 time
            # acell_no_variable = 2
            # adm_s1.update_acell(f'W{acell_no_variable}',pranav_choice_ss_s1_cno_6[acell_no_variable])
            # acell_no_variable+=1

            #test7 -> reprtition of test 6 and 3 while adding for loop in it  result->Failed
            #before it
            '''
            getting length of coloumn in of uniques_values(Code No in rough sheet)
            now running for loop upto its length
            '''
            # for i in range(len(pranav_choice_ss_s1_cno_6)):
            #     if i>1:
            #         adm_s1.update_acell(f'W{i}',pranav_choice_ss_s1_cno_6[i])
            #     else:
            #         continue
        else:
            print('Content not found')
    #fetching Pranav sir's comment, Desissions and Rahul sir's comment 
    #from rough sheet
    pranav_choice_ss_s1_cno_6 = ss_s1.col_values(6)
    pranav_comment_ss_s1_cno_7 = ss_s1.col_values(7)
    rahul_comment_ss_s1_cno_8 = ss_s1.col_values(8)

    #test8 -> repetition of test 4 while outside the loop result->Failed due to it alwyas starts from one

    # #for coloum 6
    # for i in range(len(pranav_choice_ss_s1_cno_6)):
    #     if i>0:
    #         adm_s1.update_acell(f'W{i+1}',pranav_choice_ss_s1_cno_6[i])
    #     else:
    #         continue

    # #for coloum 7
    # for i in range(len(pranav_comment_ss_s1_cno_7)):
    #     if i>0:
    #         adm_s1.update_acell(f'X{i+1}',pranav_comment_ss_s1_cno_7[i])
    #     else:
    #         continue

    # #for coloum 8
    # for i in range(len(rahul_comment_ss_s1_cno_8)):
    #     if i>0:
    #         adm_s1.update_acell(f'Y{i+1}',rahul_comment_ss_s1_cno_8[i])
    #     else:
    #         continue

    #test10 -> repetion of test8 result-> Fail
    #trying to store an variable for those into file and then accessing it
    # variable_store_file = open('D:\\git_files\\Python-Codes-1\\all_codes\\variable_store_data.txt','r')
    # variable_wrtie_file = open('D:\\git_files\\Python-Codes-1\\all_codes\\variable_store_data.txt','w')
    # #storing first line into variable
    # first_variable = variable_store_file.readline(1)
    # # first_variable = int(first_variable)
    # for i in range(len(pranav_choice_ss_s1_cno_6)):
    #     if i>0:
    #         adm_s1.update_acell(f'W{first_variable}',pranav_choice_ss_s1_cno_6[i])
    #         first_variable += 1
    #     else:
    #         continue
    # print(first_variable)
    # variable_wrtie_file.write(f'{first_variable}')

    #test 9 -> repetion of test9 result-> Failed
    # variable_store_file = open('D:\\git_files\\Python-Codes-1\\all_codes\\variable_store_data.txt','r')
    # variable_wrtie_file = open('D:\\git_files\\Python-Codes-1\\all_codes\\variable_store_data.txt','w')
    #storing first line into variable
    # print(variable_store_file.readable())
    # first_variable = variable_store_file.readline(1)
    # first_variable = int(first_variable)
    # for i in range(len(pranav_choice_ss_s1_cno_6)):
    #     if i>0:
    #         adm_s1.update_acell(f'W{first_variable}',pranav_choice_ss_s1_cno_6[i])
    #         first_variable += 1
    #     else:
    #         continue
    # print(first_variable)

    #test 11 -> upgradation of test10 result-> Sucess for inbuilt file only
    #step1 -> reading files
    # variable_store_file = open('D:\\git_files\\Python-Codes-1\\all_codes\\variable_store_data.txt','r')
    # # storing first line into variable
    # first_variable = variable_store_file.readline(1)
    # first_variable = int(first_variable)
    # for i in range(len(pranav_choice_ss_s1_cno_6)):
    #     if i>0:
    #         adm_s1.update_acell(f'W{first_variable}',pranav_choice_ss_s1_cno_6[i])
    #         first_variable += 1
    #     else:
    #         continue
    # temp_variable = variable_store_file.readline(2)

    # #for coloum 7
    # second_variable = variable_store_file.readline(3)
    # second_variable = int(second_variable)
    # for i in range(len(pranav_comment_ss_s1_cno_7)):
    #     if i>0:
    #         adm_s1.update_acell(f'X{second_variable}',pranav_comment_ss_s1_cno_7[i])
    #         second_variable += 1
    #     else:
    #         continue

    # #for coloum 8
    # third_variable = variable_store_file.readline(4)
    # third_variable = int(third_variable)
    # for i in range(len(rahul_comment_ss_s1_cno_8)):
    #     if i>0:
    #         adm_s1.update_acell(f'Y{third_variable}',rahul_comment_ss_s1_cno_8[i])
    #         third_variable += 1
    #     else:
    #         continue

    # # writing whole variable again
    # variable_write_file = open('D:\\git_files\\Python-Codes-1\\all_codes\\variable_store_data.txt','w')
    # variable_write_file.write(f"{first_variable}\n")
    # variable_write_file.write(f"{second_variable}\n")
    # variable_write_file.write(f"{third_variable}\n")

    #test12 -> changing whole method instead of unsing file use variable result->sucess
    #for coloum 6 in rough and 23 in samplesheet
    temp_variable_for_cno_23 = adm_s1.col_values(23)
    temp_variable_for_cno_23_length = len(temp_variable_for_cno_23)
    temp_variable_for_cno_23_length+=1
    for i in range(len(pranav_choice_ss_s1_cno_6)):
        if i>0:
            adm_s1.update_acell(f'W{temp_variable_for_cno_23_length}',pranav_choice_ss_s1_cno_6[i])
            temp_variable_for_cno_23_length+=1
        else:
            continue
    
    #for coloum 7 in rough and 24 in samplesheet
    temp_variable_for_cno_24 = adm_s1.col_values(24)
    temp_variable_for_cno_24_length = len(temp_variable_for_cno_24)
    temp_variable_for_cno_24_length+=1
    for i in range(len(pranav_comment_ss_s1_cno_7)):
        if i>0:
            adm_s1.update_acell(f'x{temp_variable_for_cno_24_length}',pranav_comment_ss_s1_cno_7[i])
            temp_variable_for_cno_24_length+=1
        else:
            continue
    
    #for coloum 8 in rough and 25 in samplesheet
    temp_variable_for_cno_25 = adm_s1.col_values(25)
    temp_variable_for_cno_25_length = len(temp_variable_for_cno_25)
    temp_variable_for_cno_25_length+=1
    for i in range(len(rahul_comment_ss_s1_cno_8)):
        if i>0:
            adm_s1.update_acell(f'Y{temp_variable_for_cno_25_length}',rahul_comment_ss_s1_cno_8[i])
            temp_variable_for_cno_25_length+=1
        else:
            continue

    #ending

#invoking Function
sheets_automate()
