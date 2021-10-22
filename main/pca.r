data = read.csv('~/Documents/Github/grocery/main/csv/matrix.csv')
print(data)
data$X = NULL
pca = prcomp(data, scale=TRUE)
print(pca)
{
  {
    
  }
}