import pandas as import pd
from rpy2.robjects import pandas2ri


# add whole data to test
pandas2ri.activate()

readRDS = robjects.r['readRDS']
df = readRDS('testing.rds')
df = pandas2ri.ri2py(df)

######## remove NA values
df = df.dropna()

### convert the Event column to 1 and 0
df = df*1

event = df[df["EVENT"] == 1]
normal = df[df["EVENT"] == 0]

print("number of events:",np.shape(event))
print("number of normal:",np.shape(normal))

## extract day, month, year and add it into the data set:
df['Time'] = pd.to_datetime(df['Time'])

df = df.assign(month=df['Time'].dt.month)
df = df.assign(hours=df['Time'].dt.hour)
df = df.assign(day=df['Time'].dt.day)
df = df.assign(day=df['Time'].dt.weekday)

print(df)
