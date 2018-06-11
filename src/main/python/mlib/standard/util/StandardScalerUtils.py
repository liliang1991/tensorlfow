from pyspark.ml.feature import StandardScaler
def StandardScalerModel(input_col, output_col, withStd,withMean,input_data):

    staticmethod = StandardScaler(inputCol=input_col, outputCol=output_col,
                        withStd=withStd, withMean=withMean)
    model = staticmethod.fit(input_data)
    result = model.transform(input_data)
    return result;
