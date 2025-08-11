{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Temps\\ipykernel_21268\\330950576.py:16: MarkupResemblesLocatorWarning: The input looks more like a filename than markup. You may want to open this file and pass the filehandle into Beautiful Soup.\n",
      "  text = BeautifulSoup(text, \"lxml\").text\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cleaning complete! Cleaned file saved as 'for_export_philippine_elections_cleaned.csv'\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import re\n",
    "import ftfy\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# Load the CSV file\n",
    "df = pd.read_csv('for_export_philippine_elections.csv')\n",
    "\n",
    "# Function to clean each tweet\n",
    "def clean_text(text):\n",
    "    if pd.isnull(text):\n",
    "        return \"\"\n",
    "    # Fix encoding issues\n",
    "    text = ftfy.fix_text(text)\n",
    "    # Remove HTML tags\n",
    "    text = BeautifulSoup(text, \"lxml\").text\n",
    "    # Remove URLs\n",
    "    text = re.sub(r'http\\S+|www\\S+|https\\S+', '', text)\n",
    "    # Remove mentions\n",
    "    text = re.sub(r'@\\w+', '', text)\n",
    "    # Remove hashtags (keep the word)\n",
    "    text = re.sub(r'#(\\w+)', r'\\1', text)\n",
    "    # Remove emojis and special symbols\n",
    "    text = re.sub(r'[^\\w\\s,.!?-]', '', text)\n",
    "    # Normalize whitespace\n",
    "    text = re.sub(r'\\s+', ' ', text).strip()\n",
    "    return text\n",
    "\n",
    "# Apply cleaning to the 'text' column\n",
    "df['clean_text'] = df['text'].apply(clean_text)\n",
    "\n",
    "# Remove duplicate tweets\n",
    "df = df.drop_duplicates(subset='clean_text')\n",
    "\n",
    "# Save the cleaned data\n",
    "df.to_csv('for_export_philippine_elections_cleaned.csv', index=False)\n",
    "\n",
    "print(\"clean completed'\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
