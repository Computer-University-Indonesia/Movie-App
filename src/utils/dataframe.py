import pandas as pd
import random 
def splitDataFrameList(df,target_column,separator):
    ''' df = dataframe to split,
    target_column = the column containing the values to split
    separator = the symbol used to perform the split
    returns: a dataframe with each entry for the target column separated, with each element moved into a new row. 
    The values in the other columns are duplicated across the newly divided rows.
    '''
    def splitListToRows(row,row_accumulator,target_column,separator):
        split_row = row[target_column].split(separator)
        for s in split_row:
            new_row = row.to_dict()
            new_row[target_column] = s
            row_accumulator.append(new_row)
    new_rows = []
    df.apply(splitListToRows,axis=1,args = (new_rows,target_column,separator))
    new_df = pd.DataFrame(new_rows)
    return new_df


def createPivotOf(dataFrame, targetDataFrame, column1, column2):
  dataFrame = splitDataFrameList(targetDataFrame, column2, ', ')
  dataFrame = dataFrame[[column1, column2]]
  dataFrame = dataFrame.groupby([column1, column2]).size()
  dataFrane = dataFrame.reset_index()
  # pivotName = dataFrame.pivot_table(index= dataFrame[column2], columns = dataFrame[column1], values=[column2], aggfunc='count')
  # return pivotName.fillna(0).astype(int)
  return dataFrame.reset_index()


def formatDataFrame(dataframe,groubyColumn,aggColumn):
    df_cast_grouped = dataframe.groupby(groubyColumn).agg({aggColumn: 'count'}).reset_index(
    ).rename(columns={'groubyColumn': 'id', 'title': 'value'})
    base_colors = ['rgb(26, 188, 156)', 'rgb(52, 152, 219)','rgb(155, 89, 182)', 'rgb(241, 196, 15)', 'rgb(230, 126, 34)', 'rgb(231, 76, 60)']
    df_cast_grouped['label'] = df_cast_grouped['id']
    color = []
    for i in range(len(df_cast_grouped)):
        color.append(base_colors[random.randint(0, len(base_colors) - 1)])
    df_cast_grouped['color'] = color
    return df_cast_grouped
  