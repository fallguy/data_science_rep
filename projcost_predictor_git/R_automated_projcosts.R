#### PROJECT COST AUTOMATION ####


## Data in Read ##

setwd("~/Automation_Tools/Automated Project Cost setup") # is there a way to automat this so it works for anyone?
dum_data = read.csv("dummy_data_f2.csv", header = TRUE)  # read csv file

## Cut up Data ##
dum_data = dum_data
dum_data$SF_Building
dum_data[dum_data[SF_Building]]
dum_flagship <- dum_data[dum_data$dummy_tier == "Flagship",]
dum_other <- dum_data[dum_data$dummy_tier == "Other",]

## Choose Data that you want to run in analysis
active_data = dum_data

## Summary of Data ##
str(active_data)
summary(active_data)

## Visualize Data ##
with(active_data, plot(SF_Building, Grand_Total))
with(active_data, plot(dummy_tier, Grand_Total))
with(active_data, plot(Year, Grand_Total))
with(active_data, plot(Region, Grand_Total))


## Linear Regression (one-off) ##
# x = "SF_Building"  ## is it possible to use variables in regression analysis?
# y = "Grand_Total"

onereg <- lm(Grand_Total ~ SF_Building + dummy_tier, data = active_data)
summary(onereg)
with(active_data, plot(SF_Building, Grand_Total))
abline(onereg, col = "red")
plot(onereg)


## Regression Function (x-var loop) ##
## Citation: http://www.ats.ucla.edu/stat/r/pages/looping_strings.htm (accessed 4/24/2016)
linfuncdata = dum_data

# colnames(linfuncdata)


# list of x-variables
xvar <- c("SF_Building", "Year", "dummy_tier")
yvar <- colnames(linfuncdata)[10:51]
colnames(linfuncdata)

### function that loops through x-variables to test weight of each feature
models <- lapply(xvar, function(x) {
  lm(substitute(Grand_Total ~ i, list(i = as.name(x))), data = linfuncdata)
})

# look at the first element of the list, model 
models[[1]]

# summary of singular element
lapply(models[[1]], summary)

# apply summary to each model stored in the list, models
lapply(models, summary)

# plot linear models
par(mfrow = c(2, 2))
invisible(lapply(models, plot))




### function that loops through y-variables for multiple outputs
yloopmodels <- lapply(yvar, function(x) {
  lm(substitute(i ~ SF_Building + Year + dummy_tier, list(i = as.name(x))), data = linfuncdata)
})

# apply summary to each model stored in yloopmodels
lapply(yloopmodels, summary)

# plot linear models
par(mfrow = c(2, 2))
invisible(lapply(yloopmodels, plot))


### Predicting Poject Cost ###

newproj_pred <- function(proj_num, desc, sf, reg, tier) {
  newdata <- data.frame(Project = as.integer(proj_num) , Description = as.character(desc),
                        SF_Building = as.integer(sf), Region = as.factor(reg), 
                        dummy_tier = as.factor(tier))
  predict(onereg, newdata)
}



thisthing <- data.frame(Project = 1254, Description = "test34", SF_Building = 20000, Region = as.factor("LA"), dummy_tier = as.factor("Flagship"))
thisthing

predict(onereg, thisthing)



predict(onereg, data.frame(newprojsf))