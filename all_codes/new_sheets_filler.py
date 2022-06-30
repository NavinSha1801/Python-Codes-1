#importing Libraries
import gspread

#defining Function
def sheets_automate():
    #credentials there is an api to access it in google developer console 
    acc = gspread.service_account('D:\\git_files\\Python-Codes-1\\all_codes\\new_id.json')

    #Openning all files 

    first_sheet = acc.open('Candidate - Softedge')
    second_sheets = acc.open('rough')   
    third_sheets = acc.open('Recruitment Form (Responses)')
    forth_sheets = acc.open('Java Recruiter Sheet')
    all_data_merge = acc.open('samplesheet')

    #accessing sheets 
    #openning sheets of Candidates - Softedge
    fs_s1 = first_sheet.worksheet('Sheet1')
    fs_s2 = first_sheet.worksheet('Rejected Candidate')
    fs_s3 = first_sheet.worksheet('Not a proper Candidate')
    fs_s4 = first_sheet.worksheet('Closure Candidate')

    #acessing sheets of rough
    ss_s1 = second_sheets.worksheet('Sheet1')

    #openning sheets of Recruitment Form (Responses)
    ts_s1 = third_sheets.worksheet('Form Responses 1')
    ts_s2 = third_sheets.worksheet('Java')
    ts_s3 = third_sheets.worksheet('Javascript')
    ts_s4 = third_sheets.worksheet('Flutter Developer')
    ts_s5 = third_sheets.worksheet('Python Devloper')
    ts_s6 = third_sheets.worksheet('DevOps')
    ts_s7 = third_sheets.worksheet('Rejected Candidate')

    #opening sheets of Java Recruiter Sheet
    frs_s1 = forth_sheets.worksheet('Interview')
    frs_s1 = forth_sheets.worksheet('Rejected')
    frs_s1 = forth_sheets.worksheet('Selected')
    frs_s1 = forth_sheets.worksheet('Deployed')

    #accessing sheets of samplesheet
    adm_s1 = all_data_merge.worksheet('Sheet1')



    #getting name coloumns for rough sheet -> getting data type is list
    uniqueid_ss_s1 = ss_s1.col_values(2)

    '''
    Creating a loop in which every name got fetched and then it will fecth all uniqueid and 
    going to check into candidates sheet and if available then fetch all data from candidates
    sheet and paste into sample sheet
    '''
    # print(fs_s1.col_values(2))
    for i in uniqueid_ss_s1:
        if i in fs_s4.col_values(2):
            #finding data
            location_candidates = fs_s4.find(i)
            location_candidates = str(location_candidates)

            #extracting Row value 
            lst = location_candidates.split(' ')
            if len(lst)>1:
                row_coloms = lst[1]
                row_value = 0
                #for rows
                for i in row_coloms:
                    if i.isdigit():
                        i = int(i)
                        row_value = (row_value*10)+i
                    elif i =='C':
                        break
            #fetching data from candidates and rough
            row_data = fs_s4.row_values(row_value)

            #appending data to sample sheet
            adm_s1.append_row(row_data)

        elif i in ts_s1.col_values(2):
            #finding data
            location_candidates = ts_s1.find(i)
            location_candidates = str(location_candidates)

            #extracting Row value 
            lst = location_candidates.split(' ')
            if len(lst)>1:
                row_coloms = lst[1]
                row_value = 0
                #for rows
                for i in row_coloms:
                    if i.isdigit():
                        i = int(i)
                        row_value = (row_value*10)+i
                    elif i =='C':
                        break
            #fetching data from candidates and rough
            row_data = ts_s1.row_values(row_value)

            #appending data to sample sheet
            adm_s1.append_row(row_data)
        else:
            print('nahi hai')


    #fetching Pranav sir's comment, Desissions and Rahul sir's comment 
    #from rough sheet
    pranav_choice_ss_s1_cno_6 = ss_s1.col_values(6)
    pranav_comment_ss_s1_cno_7 = ss_s1.col_values(7)
    rahul_comment_ss_s1_cno_8 = ss_s1.col_values(8)

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
