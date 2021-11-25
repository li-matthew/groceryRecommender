library(ggplot2)

components = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/visualization/components.csv')
print(components)
# colnames(components) = c('Component #', 'Explained Variance')

ggplot(components, aes(x=X, y=X0))+geom_point()+xlab('Component #') + ylab('Explained Variance')


sv = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/sv.csv')
print(sv)
# colnames(components) = c('Component #', 'Explained Variance')

ggplot(sv, aes(x=X, y=X0))+geom_point()+xlab('x') + ylab('sv')

rmse = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/rmse.csv')
print(rmse)
print(row.names(rmse))
print(colnames(rmse))
ggplot(rmse, aes(x = fold, y = error, col=type)) + geom_line() + ylim(0.25, 0.75)

mae = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/mae.csv')
print(mae)
print(row.names(mae))
print(colnames(mae))
ggplot(mae, aes(x = fold, y = error, col=type)) + geom_line() + ylim(0.15, 0.65)

lr = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/lr.csv')
print(lr)
ggplot(lr, aes(x=lr, y = rmse)) + geom_line()

sgdloss = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/loss.csv')
print(sgdloss)
ggplot(sgdloss, aes(x=as.numeric(row.names(sgdloss)), y = loss)) + geom_line()
