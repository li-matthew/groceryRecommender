library(ggplot2)

components = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/components.csv')
print(components)
# colnames(components) = c('Component #', 'Explained Variance')

ggplot(components, aes(x=X, y=X0))+geom_point()+xlab('Component #') + ylab('Explained Variance')


sv = read.csv('/Users/matthewli/Documents/GitHub/grocery/main/csv/sv.csv')
print(sv)
# colnames(components) = c('Component #', 'Explained Variance')

ggplot(sv, aes(x=X, y=X0))+geom_point()+xlab('x') + ylab('sv')
