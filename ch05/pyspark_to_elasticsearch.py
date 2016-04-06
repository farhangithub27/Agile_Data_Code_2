# Load the parquet file
on_time_dataframe = sqlContext.read.parquet('../data/on_time_performance.parquet')

# Format data for Elasticsearch, as a tuple with a dummy key in the first field
on_time_performance = on_time_dataframe.rdd.map(lambda x: ('ignored_key', x.asDict()))

on_time_performance.saveAsNewAPIHadoopFile(
  path='-', 
  outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
  keyClass="org.apache.hadoop.io.NullWritable", 
  valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable", 
  conf={ "es.resource" : "agile_data_science/on_time_performance" })
