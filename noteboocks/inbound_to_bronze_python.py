# Databricks notebook source
# MAGIC %md
# MAGIC # Python

# COMMAND ----------

# MAGIC %md
# MAGIC **Conferindo se os dados foram montados e se temos acesso a pasta inbound**

# COMMAND ----------

dbutils.fs.ls("/mnt/dados/inbound")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lendo os dados na camada de inbound

# COMMAND ----------

path = "dbfs:/mnt/dados/inbound/dataset_imoveis_bruto.json"
dados = spark.read.json(path)
display(dados)


# COMMAND ----------

# MAGIC %md
# MAGIC ## Removendo colunas

# COMMAND ----------

df_bronze = dados.drop("imagens", "usuario")
display(df_bronze)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Criando uma coluna de identificação

# COMMAND ----------

from pyspark.sql.functions import col

df_bronze = df_bronze.withColumn("id", col("anuncio.id"))
display(df_bronze)


# COMMAND ----------

# MAGIC %md
# MAGIC ## Salvando na camada bronze

# COMMAND ----------

path = "dbfs:/mnt/dados/bronze/dataset_imoveis"
df_bronze.write.format("delta").mode("overwrite").save(path)
