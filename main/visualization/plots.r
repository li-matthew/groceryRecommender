library(ggplot2)

components = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/visualization/components.csv')
print(components)
# colnames(components) = c('Component #', 'Explained Variance')

ggplot(components, aes(x=X, y=X0))+geom_point()+xlab('Component #') + ylab('Explained Variance')


sv = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/sv.csv')
print(sv)
# colnames(components) = c('Component #', 'Explained Variance')

ggplot(sv, aes(x=X, y=X0))+geom_point()+xlab('x') + ylab('sv')

rmse = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/visualization/rmse.csv')
print(rmse)
print(row.names(rmse))
print(colnames(rmse))
ggplot(rmse, aes(x = fold, y = error, col=type)) + geom_line()+xlab('Fold') + ylab('RMSE') + ylim(0.8, 1.05)+ scale_x_continuous(breaks = seq(0, 3, by = 1))

mse = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/visualization/mse.csv')
print(mse)
print(row.names(mse))
print(colnames(mse))
ggplot(mse, aes(x = fold, y = error, col=type)) + geom_line()+xlab('Fold') + ylab('MSE') + ylim(0.8, 1.05)+ scale_x_continuous(breaks = seq(0, 3, by = 1))

lr = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/visualization/lr.csv')
print(lr)
ggplot(lr, aes(x=lr, y = rmse)) + geom_line()+xlab('Learning Rate') + ylab('RMSE') + xlim(0, 0.016)

sgdloss = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/visualization/loss.csv')
print(sgdloss)
sgdloss$loss = sgdloss$loss * 10
ggplot(sgdloss, aes(x=as.numeric(row.names(sgdloss)), y = loss)) + geom_line()+xlab('Epoch') + ylab('Loss')

x = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/log1mmanipulated.csv')
print(x)
# x= subset(x, match >=5)
# colnames(components) = c('Component #', 'Explained Variance')
hist(x$match, breaks=100)
ggplot(x, aes(x=as.numeric(row.names(x)), y=match))+geom_line()
