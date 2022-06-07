#q3
import datefinder
import calendar
import question2 as q2

# docs_CISI=q2.getdocs_lem_CISI()
# docs_cacm=q2.getdocs_lem_cacm()

def date_processor(text):
    dic_month={month: index for index, month in enumerate(calendar.month_abbr) if month}
    try:
        match = datefinder.find_dates(text,source=1)

        for item in match:
            replacement = ""

            if (item[1].__len__() > 4) and not('PM' in item[1]) and not('AM' in item[1]) and (any(ch.isdigit() for ch in item[1])) :
                replacement += str(item[0].day)
                replacement += "-"
                if type(item[0].month)==int :
                    replacement += str(item[0].month)
                else :
                    replacement += dic_month[item[0].month]
                replacement += "-"
                replacement += str(item[0].year)
                text = text.replace(item[1], replacement)
            
    except:
        pass

    return text




# formated_date_docs_CISI= []
# formated_date_docs_cacm= []
# for d in docs_CISI:
#     formated_date_docs_CISI.append(date_processor(d))
# for d in docs_cacm:
#     formated_date_docs_cacm.append(date_processor(d))
# #print(formatedTokens)