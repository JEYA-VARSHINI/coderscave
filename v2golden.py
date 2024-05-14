import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\HP\\Downloads\\email spam\\emails.csv")

# Visualize spam distribution with a count plot
plt.figure(figsize=(6, 4))
sns.countplot(x='spam', data=df, palette=['skyblue', 'orange'])
plt.xlabel('Spam')
plt.ylabel('Count')
plt.title('Spam Distribution')
plt.xticks([0, 1], ['Not Spam', 'Spam'])
plt.show()

# Prepare data
X = df['text'].astype(str)
y = df['spam'].replace({0: "Not Spam", 1: "Spam"}).astype("object")

# Calculate email lengths
email_lengths = X.str.len()

# Plot violin plot of email lengths
plt.figure(figsize=(8, 6))
sns.violinplot(y=email_lengths, palette=['lightblue'])
plt.ylabel('Email Length')
plt.title('Violin Plot of Email Lengths')
plt.grid(True)
plt.show()

# Plot violin plot of email lengths vs. spam
plt.figure(figsize=(8, 6))
sns.violinplot(x=y, y=email_lengths, palette=['lightblue', 'orange'])
plt.xlabel('Spam')
plt.ylabel('Email Length')
plt.title('Violin Plot of Email Lengths vs. Spam')
plt.grid(True)
plt.show()

# Pair plot to visualize relationships between features (assuming there are more numerical features in the dataset)
# For demonstration, we will use email_lengths as another feature
df['email_lengths'] = email_lengths
sns.pairplot(df[['email_lengths', 'spam']], hue='spam', palette=['lightblue', 'orange'])
plt.show()

