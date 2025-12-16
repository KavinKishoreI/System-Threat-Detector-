{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "l3OLag3s1FIB"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "F1nnYkmD1jGh",
    "outputId": "9b61e356-36e2-4bc4-91eb-544283a41f11",
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 65535 entries, 0 to 65534\n",
      "Data columns (total 76 columns):\n",
      " #   Column                              Non-Null Count  Dtype  \n",
      "---  ------                              --------------  -----  \n",
      " 0   MachineID                           65535 non-null  object \n",
      " 1   ProductName                         65535 non-null  object \n",
      " 2   EngineVersion                       65535 non-null  object \n",
      " 3   AppVersion                          65535 non-null  object \n",
      " 4   SignatureVersion                    65535 non-null  object \n",
      " 5   IsBetaUser                          65535 non-null  int64  \n",
      " 6   RealTimeProtectionState             65493 non-null  float64\n",
      " 7   IsPassiveModeEnabled                65535 non-null  int64  \n",
      " 8   AntivirusConfigID                   65490 non-null  float64\n",
      " 9   NumAntivirusProductsInstalled       65490 non-null  float64\n",
      " 10  NumAntivirusProductsEnabled         65490 non-null  float64\n",
      " 11  HasTpm                              65535 non-null  int64  \n",
      " 12  CountryID                           65535 non-null  int64  \n",
      " 13  CityID                              65134 non-null  float64\n",
      " 14  GeoRegionID                         65535 non-null  int64  \n",
      " 15  LocaleEnglishNameID                 65535 non-null  int64  \n",
      " 16  PlatformType                        65535 non-null  object \n",
      " 17  Processor                           65535 non-null  object \n",
      " 18  OSVersion                           65535 non-null  object \n",
      " 19  OSBuildNumber                       65535 non-null  int64  \n",
      " 20  OSProductSuite                      65535 non-null  int64  \n",
      " 21  OsPlatformSubRelease                65535 non-null  object \n",
      " 22  OSBuildLab                          65535 non-null  object \n",
      " 23  SKUEditionName                      65535 non-null  object \n",
      " 24  IsSystemProtected                   65490 non-null  float64\n",
      " 25  AutoSampleSubmissionEnabled         65535 non-null  int64  \n",
      " 26  SMode                               64899 non-null  float64\n",
      " 27  IEVersionID                         65460 non-null  float64\n",
      " 28  FirewallEnabled                     65415 non-null  float64\n",
      " 29  EnableLUA                           65523 non-null  float64\n",
      " 30  MDC2FormFactor                      65535 non-null  object \n",
      " 31  DeviceFamily                        65535 non-null  object \n",
      " 32  OEMNameID                           65386 non-null  float64\n",
      " 33  OEMModelID                          65377 non-null  float64\n",
      " 34  ProcessorCoreCount                  65473 non-null  float64\n",
      " 35  ProcessorManufacturerID             65473 non-null  float64\n",
      " 36  ProcessorModelID                    65473 non-null  float64\n",
      " 37  PrimaryDiskCapacityMB               65458 non-null  float64\n",
      " 38  PrimaryDiskType                     65520 non-null  object \n",
      " 39  SystemVolumeCapacityMB              65458 non-null  float64\n",
      " 40  HasOpticalDiskDrive                 65535 non-null  int64  \n",
      " 41  TotalPhysicalRAMMB                  65434 non-null  float64\n",
      " 42  ChassisType                         65534 non-null  object \n",
      " 43  PrimaryDisplayDiagonalInches        65489 non-null  float64\n",
      " 44  PrimaryDisplayResolutionHorizontal  65489 non-null  float64\n",
      " 45  PrimaryDisplayResolutionVertical    65489 non-null  float64\n",
      " 46  PowerPlatformRole                   65535 non-null  object \n",
      " 47  InternalBatteryNumberOfCharges      65195 non-null  float64\n",
      " 48  NumericOSVersion                    65535 non-null  object \n",
      " 49  OSArchitecture                      65535 non-null  object \n",
      " 50  OSBranch                            65535 non-null  object \n",
      " 51  OSBuildNumberOnly                   65535 non-null  int64  \n",
      " 52  OSBuildRevisionOnly                 65535 non-null  int64  \n",
      " 53  OSEdition                           65535 non-null  object \n",
      " 54  OSSkuFriendlyName                   65535 non-null  object \n",
      " 55  OSInstallType                       65535 non-null  object \n",
      " 56  OSInstallLanguageID                 65463 non-null  float64\n",
      " 57  OSUILocaleID                        65535 non-null  int64  \n",
      " 58  AutoUpdateOptionsName               65535 non-null  object \n",
      " 59  IsPortableOS                        65535 non-null  int64  \n",
      " 60  OSGenuineState                      65535 non-null  object \n",
      " 61  LicenseActivationChannel            65535 non-null  object \n",
      " 62  IsFlightsDisabled                   65312 non-null  float64\n",
      " 63  FlightRing                          65535 non-null  object \n",
      " 64  FirmwareManufacturerID              65271 non-null  float64\n",
      " 65  FirmwareVersionID                   65302 non-null  float64\n",
      " 66  IsSecureBootEnabled                 65535 non-null  int64  \n",
      " 67  IsVirtualDevice                     65519 non-null  float64\n",
      " 68  IsTouchEnabled                      65535 non-null  int64  \n",
      " 69  IsPenCapable                        65535 non-null  int64  \n",
      " 70  IsAlwaysOnAlwaysConnectedCapable    65445 non-null  float64\n",
      " 71  IsGamer                             65167 non-null  float64\n",
      " 72  RegionIdentifier                    65167 non-null  float64\n",
      " 73  DateAS                              65535 non-null  object \n",
      " 74  DateOS                              65522 non-null  object \n",
      " 75  target                              65535 non-null  int64  \n",
      "dtypes: float64(30), int64(18), object(28)\n",
      "memory usage: 38.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"../data/train_data.csv\")\n",
    "affected_df = df[df['target'] ==1 ] # separate the affected rows and not affected rows.\n",
    "not_affected_df = df[df['target'] == 0 ]\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "0rImo-O49k0U"
   },
   "outputs": [],
   "source": [
    "def plot_and_compare (df, affected, not_affected_df , column_name):\n",
    "    \"\"\" Plots 2 things \n",
    "        1. histogram to visualise the distribution\n",
    "        2. box plot to visualise the IQR for different classes. \n",
    "    \"\"\"\n",
    "    sns.histplot(data=df, x=column_name, kde=True)\n",
    "    #histogram plot to show distribution\n",
    "    plt.show()\n",
    "    x_limit = df[column_name].max() * 1.05  # Add 5% padding for better visuals\n",
    "\n",
    "      # Boxplot to compare the distribution\n",
    "    sns.boxplot(data=affected_df, x=column_name)\n",
    "    plt.title('affected plot')\n",
    "    plt.xlim(0, x_limit) # Ensures same scale has been followed to avoid biased conclusion.\n",
    "    plt.show()\n",
    "\n",
    "    sns.boxplot(data=not_affected_df, x=column_name)\n",
    "    plt.title('Not affected plot')\n",
    "    plt.xlim(0, x_limit) # Ensures same scale has been followed to avoid biased conclusion.\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "Investigating Numeric columns to identify patterns : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "7wm2UK85YpPe",
    "outputId": "e49a8ef7-04dd-4883-f6e2-5082592faf5f"
   },
   "outputs": [],
   "source": [
    "plot_and_compare(df,  affected_df , not_affected_df , 'NumAntivirusProductsEnabled') # not useful"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "3q8-fiYZ-rmA",
    "outputId": "7c75a972-0c9c-47c8-99bc-13d6794141c1"
   },
   "outputs": [],
   "source": [
    "plot_and_compare(df,  affected_df , not_affected_df , \"NumAntivirusProductsInstalled\") # Useful column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "vVubF2jQa_ru",
    "outputId": "7ff44b22-737c-4375-dc7d-52dec950cbea"
   },
   "outputs": [],
   "source": [
    "plot_and_compare(df,  affected_df , not_affected_df , 'ProcessorCoreCount') # needs more investigation interesting data\n",
    "df['ProcessorCoreCount'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "CirCpgIwfJq2",
    "outputId": "6694408e-38a5-4ce0-9a31-e477f9130279"
   },
   "outputs": [],
   "source": [
    "print(df['PrimaryDiskCapacityMB'].nunique())\n",
    "plot_and_compare(df,  affected_df , not_affected_df , 'PrimaryDiskCapacityMB')# might be useful\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "WlPzAcFjnT6-",
    "outputId": "82c51f5c-1cef-49a7-ae8c-cbb3708dda96"
   },
   "outputs": [],
   "source": [
    "plot_and_compare(df,  affected_df , not_affected_df , 'TotalPhysicalRAMMB')\n",
    "# non predictive because the box plots ( whisker lines , box) are litreally same"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "4MFkJFyxlBFW",
    "outputId": "a82c91c4-4c32-436f-e136-8dd7865c2b59"
   },
   "outputs": [],
   "source": [
    "plot_and_compare(df,  affected_df , not_affected_df , 'SystemVolumeCapacityMB')\n",
    "# non predictive because the box plots ( whisker lines , box) are litreally same"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "GXA2aSFX7SFC",
    "outputId": "4cc10b2d-67ff-4d43-ce88-2267f4d5c6de"
   },
   "outputs": [],
   "source": [
    "def count_classes (df, affected_df , unaffected_df , column ):\n",
    "  \"\"\" Nothinng fancy just counts the classes to print the number of classes\"\"\" \n",
    "  count = df[column].nunique()\n",
    "  print(\"No of \"+ column , count, sep = \":\")\n",
    "\n",
    "# Just a check \n",
    "# count_classes(df,affected_df , not_affected_df, \"MachineID\" )\n",
    "# count_classes(df,affected_df , not_affected_df, \"CityID\" )\n",
    "# count_classes(df, affected_df, not_affected_df , \"CountryID\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Bm6d4b_XvsYR"
   },
   "source": [
    "Exploring columns with lesser cardinality features to find patterns.\n",
    "'PlatformType' : Platform Type Derived from OS and Processor Information\n",
    " 'Processor' : Processor Architecture of the Installed OS\n",
    " 'DeviceFamily'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "SZu7Yd-FwIOc",
    "outputId": "7cf0ff10-2a56-470d-9e17-514d0b9dbff5"
   },
   "outputs": [],
   "source": [
    "def count_ploting(df , affected_df , not_affected_df , column ):\n",
    "  crosstab = pd.crosstab(df[column], df['target'])\n",
    "  print(\"--- Raw Counts ---\")\n",
    "  print(crosstab)\n",
    "  crosstab_norm = pd.crosstab(df[column], df['target'], normalize='index')\n",
    "  print(\"\\n--- Proportions (percentages) ---\")\n",
    "  changes = crosstab_norm[1]-crosstab_norm[0]\n",
    "  print(crosstab_norm)\n",
    "  print(\"\\n--- Differences  (percentages) ---\")\n",
    "  print(changes) \n",
    "    \n",
    "  sns.countplot(df , x= column)\n",
    "  plt.show()\n",
    "  sns.countplot(df , x= column, hue = 'target') # categorial count plot compares based on categories.\n",
    "  plt.show()\n",
    "    \n",
    "  \n",
    "  crosstab_norm.plot(kind = 'bar', stacked = True)\n",
    "  plt.show()  \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "tWskW9496pwJ",
    "outputId": "2c024212-301e-469e-bac8-423d27220362"
   },
   "outputs": [],
   "source": [
    "count_classes(df, affected_df , not_affected_df, 'PlatformType' )\n",
    "count_ploting(df, affected_df , not_affected_df, 'PlatformType') # windows2016 isnt affected as much as others\n",
    "# pattern should be investigates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "count_classes(df, affected_df , not_affected_df, 'RealTimeProtectionState' )\n",
    "count_ploting(df, affected_df , not_affected_df, 'RealTimeProtectionState')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "lbEmuc1b4FFu"
   },
   "outputs": [],
   "source": [
    "count_classes(df, affected_df , not_affected_df, 'PrimaryDiskType')\n",
    "count_ploting(df, affected_df , not_affected_df, 'PrimaryDiskType')  # low impact"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_classes(df, affected_df , not_affected_df, 'Processor')\n",
    "count_ploting(df, affected_df , not_affected_df, 'Processor')\n",
    "# useful predictor x32 infected more than x86 processor "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def group_categories_plot(df, affected_df , not_affected_df , column, no_columns):\n",
    "    top_editions = df[column].value_counts().nlargest(no_columns).index\n",
    "    print(\"Categories to keep:\", top_editions)\n",
    "    df[f'{column}_grouped'] = np.where(df[column].isin(top_editions), \n",
    "                                         df[column], \n",
    "                                         'Other')\n",
    "    count_ploting(df, affected_df, not_affected_df, column+'_grouped' )\n",
    "\"\"\"\n",
    "count_classes(df, affected_df , not_affected_df, 'SKUEditionName')\n",
    "count_ploting(df, affected_df , not_affected_df, 'SKUEditionName') \n",
    "\"\"\"\n",
    "# count plotting lead to grouping the columns due to a high cardinality\n",
    "group_categories_plot(df, affected_df, not_affected_df, 'SKUEditionName' , 2) # I see two major columns so I need to group other columns\n",
    "\n",
    "# useful"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "\"\"\"count_classes(df, affected_df , not_affected_df, 'OSEdition')\n",
    "count_ploting(df, affected_df , not_affected_df, 'OSEdition')\"\"\"\n",
    "group_categories_plot(df, affected_df, not_affected_df,'OSEdition' , 3) # I see 3 major columns so I need to group other columns \n",
    "#OSEdition good predictor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"count_classes(df, affected_df , not_affected_df, 'OSBuildNumber')\n",
    "count_ploting(df, affected_df , not_affected_df, 'OSBuildNumber')\n",
    "\"\"\"\n",
    "group_categories_plot(df, affected_df, not_affected_df, 'OSBuildNumber' , 5) # I see 5 major columns so I need to group other columns \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"count_classes(df, affected_df , not_affected_df, 'ChassisType')\n",
    "count_ploting(df, affected_df , not_affected_df, 'ChassisType') \n",
    "\"\"\"\n",
    "count_classes(df, affected_df , not_affected_df, 'ChassisType')\n",
    "group_categories_plot(df, affected_df, not_affected_df, 'ChassisType' , 4) # I see 3 major columns so I need to group other columns \n",
    "# less useful. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "GEEq94-h6rOo"
   },
   "source": [
    "High cardinality columns below\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#count_ploting (df, affected_df, not_affected_df , \"AntivirusConfigID\") \n",
    "# Suspicious because intutively antivirus cofig could be a strong predictor so analysing by grouping the most occuring classes,\n",
    "group_categories_plot(df, affected_df, not_affected_df, \"AntivirusConfigID\" , 1)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "group_categories_plot(df, affected_df, not_affected_df, \"AppVersion\" , 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "binary_columns = [\n",
    "    #'IsBetaUser',\n",
    "    #'IsPassiveModeEnabled',\n",
    "    #'HasTpm',\n",
    "    'IsSystemProtected',\n",
    "    'RealTimeProtectionState',\n",
    "    'FirewallEnabled'\n",
    "    #'IsSecureBootEnabled',\n",
    "    #'HasOpticalDiskDrive',\n",
    "    \n",
    "    \n",
    "]\n",
    "\n",
    "# 2. Loop through each column and create a normalized plot\n",
    "for column in binary_columns:\n",
    "    # Create the normalized crosstab to get the rates\n",
    "    plt.figure(figsize=(7, 5))\n",
    "    sns.countplot(data=df, x=column, hue='target')\n",
    "    plt.title(f'Absolute Counts for {column}')\n",
    "    plt.show()\n",
    "    \n",
    "    crosstab_norm = pd.crosstab(df[column], df['target'], normalize='index')\n",
    "    \n",
    "    # Plot the rates as a stacked bar chart\n",
    "    crosstab_norm.plot(kind='bar', \n",
    "                       stacked=True, \n",
    "                       figsize=(7, 5),\n",
    "                       title=f'Infection Rate by {column}')\n",
    "\n",
    "    plt.ylabel('Proportion')\n",
    "    plt.xticks(rotation=0)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 898
    },
    "id": "lwZYir3Rsu1b",
    "outputId": "3c9d7ee4-80c2-4c92-f75b-18f25fae49d4"
   },
   "outputs": [],
   "source": [
    "count_classes(df, affected_df, not_affected_df, 'LocaleEnglishNameID')\n",
    "sns.countplot(df, x=\"LocaleEnglishNameID\")\n",
    "plt.show()\n",
    "sns.countplot(affected_df , x = \"LocaleEnglishNameID\")\n",
    "sns.countplot(not_affected_df , x = \"LocaleEnglishNameID\")\n",
    "\n",
    "plt.show()\n",
    "\n",
    "# drop Locale English Name Id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 898
    },
    "id": "GcwO9s-4uJGq",
    "outputId": "bc54a805-f66e-4ded-8ba7-82b676fef38a"
   },
   "outputs": [],
   "source": [
    "# count_classes(df, affected_df, not_affected_df, 'IEVersionID')\n",
    "# sns.countplot(df, x='IEVersionID')\n",
    "# plt.show()\n",
    "# sns.countplot(affected_df , x = 'IEVersionID')\n",
    "# sns.countplot(not_affected_df , x ='IEVersionID')\n",
    "group_categories_plot(df, affected_df, not_affected_df, 'IEVersionID' ,5) \n",
    "plt.show()\n",
    "# drop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_ploting(df, affected_df, not_affected_df, 'IsSystemProtected' ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_classes(df, affected_df,not_affected_df, 'OSArchitecture' )\n",
    "count_ploting(df,affected_df, not_affected_df, 'OSArchitecture') # Redundant to processor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_ploting(df, affected_df, not_affected_df, 'DeviceFamily') #drop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#count_ploting(df, affected_df, not_affected_df, 'ProcessorCoreCount')\n",
    "group_categories_plot(df, affected_df, not_affected_df, \"ProcessorCoreCount\" , 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#plot_and_compare (df, affected_df, not_affected_df , 'PrimaryDisplayDiagonalInches') #Not useful\n",
    "#plot_and_compare (df, affected_df, not_affected_df , 'PrimaryDisplayResolutionVertical')# Not useful\n",
    "\n",
    "count_classes(df,affected_df, not_affected_df, 'PowerPlatformRole')\n",
    "count_ploting(df,affected_df,not_affected_df, 'PowerPlatformRole')\n",
    "group_categories_plot(df,affected_df, not_affected_df,'PowerPlatformRole', 3) # good Predictor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_classes(df, affected_df, not_affected_df ,'InternalBatteryNumberOfCharges')\n",
    "group_categories_plot(df, affected_df, not_affected_df, 'InternalBatteryNumberOfCharges',5) #useless"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_ploting(df, affected_df, not_affected_df, 'OSVersion') # useless"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_ploting(df, affected_df, not_affected_df, 'FirewallEnabled') # weak "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "group_categories_plot(df, affected_df, not_affected_df,'OSInstallType', 8) # good predictor strong top 8 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_and_compare_dates (df, affected, not_affected_df , column_name):\n",
    "    \"\"\" Plots 2 things \n",
    "        1. histogram to visualise the distribution\n",
    "        2. box plot to visualise the IQR for different classes. \n",
    "    \"\"\"\n",
    "    sns.histplot(data=df, x=column_name, kde=True)\n",
    "    #histogram plot to show distribution\n",
    "    plt.show()\n",
    "\n",
    "      # Boxplot to compare the distribution\n",
    "    sns.boxplot(data=df, x=column_name)\n",
    "    plt.title('affected plot')\n",
    "    plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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r14t48aNk9GjR8ukSZNcZZYsWSK33367CVxr1qyRG264wSwbN26s5HcAAAB4Cx/LsizxANrSNH36dBNWTmblypVy8cUXS2JiojRp0kS2bNki7dq1M/d369bNlJkzZ45cc801sm/fPtM69e6778rTTz8tycnJEhgYaMo89dRTplVr69at5vZtt91mApyGLluPHj2kS5cuMnHiREf113AWGRkpGRkZptULAIDaLDExUd7/YZfExDWStJT9cm/v80wDhqc5k99vr+rTpC9Iw5UehlNLly411+3ApPr16ye+vr6yfPlyV5k+ffq4ApPq37+/abU6evSoq4w+zp2W0ftPJj8/37zR7gsAAKi5vCY05eXlmT5OehjNToLaelS/fv0y5fz9/SUmJsass8vExcWVKWPfPl0Ze315xowZY5KpvWhfKQAAUHN5RWjSTuG33nqr6JFEPdzmCUaNGmVavuwlKSmpuqsEAAAqkb94SWDSY6MLFy4sc7wxPj5eUlNTy5QvKioyI+p0nV0mJSWlTBn79unK2OvLExQUZBYAAFA7+HpDYNqxY4d8++23EhsbW2Z9z549JT093YyKs2mwKikpke7du7vK6Ig63ZZNR9q1bt1aoqOjXWUWLFhQZttaRu8HAACo9tCk8ymtXbvWLGr37t3m+t69e03IueWWW2TVqlXy6aefSnFxseljpEtBQYEp37ZtWxkwYIAMGzZMVqxYIT/99JOMHDlSBg0aZEbOqTvuuMN0AtfpBHRqgi+++ELefPNNefTRR131eOihh8you/Hjx5sRdTolgT6vbgsAAMCwqtGiRYt0uoMTliFDhli7d+8ud50u+jjbkSNHrNtvv90KCwuzIiIirHvuucfKysoq8zzr1q2zLr30UisoKMhq1KiR9fLLL59Ql6lTp1qtWrWyAgMDrfbt21uzZs06o9eSkZFh6qaXAADUdnv27LGe+fdC67V528yl3vZEZ/L77THzNHk75mkCAOA3zNMEAABQSxGaAAAAHCA0AQAAOEBoAgAAcIDQBAAA4AChCQAAwAFCEwAAgAOEJgAAAAcITQAAAA4QmgAAABwgNAEAADhAaAIAAHCA0AQAAOAAoQkAAMABQhMAAIADhCYAAAAHCE0AAAAOEJoAAAAc8HdSCAAA1E4lJSWSlJRkrickJIivb+1tb6m9rxwAAJyWBqbx05eYxQ5P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dC0FBQWnrN/nn39uBQYGWh9++KG1adMma9iwYVZUVJSVkpJi6j5x4kSrcePG1uWXX2717t3batCggTVw4EDroosusoqLiyuk7naZ1q1bW//73/+sXbt2mW3NmzfvlHX/6aefLD8/P2vs2LHW5s2brWeeecYKCAiwNmzY4Hrf//nPf1r33Xef1bFjxxPOPejpdf/9739v6nPFFVdYjRo1sn755RcrLS3N4+uu+1KnTp2sCy64wLrkkkushg0bWvfcc49rv6+IumdlZZXZz3Vp166dNWTIkLPa3/v27ev6nP71r38174ner/vM0aNHK+w9r+h6259TrXu3bt2sm266qcz+kpGR4fF1r4rvGN23g4KCrFGjRlk7d+60Vq9ebfXp08fso2ezr+t+be8vL774otWyZUsrJibG7C9r1qypsPe8outdld8vuyqh7qqkpMTUR/eVFStWWFu3brWGDx9+wu/q2SI0eZjU1FTzwfr+++/N7fT0dLNDTJs2zVVmy5YtpszSpUvLPZHwqUKT/YF1Sk9WfP/997tu65eU/siNGTPG3J47d67l6+trvnztus+aNcvy8fGxvvrqqwqpu34w/P39zc5/Jm699Vbz5eque/fu1p///OcTyuoHX+v1/vvvV+j7Xpl11x+j66+/vtL2mcqq+7Zt20xd9AfFrvuiRYusevXqWW+++WaF1P14+geJbmPx4sXntL/b7Hrboami3vPKrPfvfvc766GHHqq0/aWy6l4V3zH6eN3X9bltM2bMMM9xqj8snX7HuO8v+h1cUe95Zda7sr9fplVS3d2/X2z6HPr98t5771nnisNzHiYjI8NcxsTEmMvVq1dLYWGh9OvXz1VGmyWbNGkiS5cuPePt//73vzdNxZdeeqnMmDHjlGULCgrM87s/t6+vr7ltP3d+fr5pttUmWLvueq4+Lffll19WSN2//vprOe+882TmzJnSvHlz04x/7733mhMkn4o+h/tzq/79+5f73HqyRvfzD1XU+17Zdf/uu+9MvexDHEeOHPH4uus+o7Rp3d5n9HCX7kOzZs2q0P3d9v7775tDjL179z6n/d1m19tW0Z/Tyqr3p59+aranPvnkEzl27JjH170qvmP0MJJub/LkyVJcXGye59///rfZrh6mOtfPaWXtL5Vd78r8fulaSXV3/36x6fPo/vPjjz/KuSI0eRA9193D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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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unXr5ho0aODuvffe2GM33HCDO+mkk8w6mDp1qrv11ltj9wcOHOiOOeYYN3fuXHfllVfGHr///vv9MvV4aP/99/ePR9fn4MGDE65/PZebPn36uIULF8bu63MYPXp0wmkvvPBC991338Xu77333r58oe3bt/uy/v7772733Xf3Ze3fv7/76KOPYtMcfvjh7u677044/3POOcf98ssvLq/0WUybNs2X7aKLLnJBEJhptB3ps50xY0bSeZUsWdK/pxEjRrh58+bFHm/VqpV74IEH3Pnnn+++//77pPNItt4//fRTd+2115rHta2/+uqrefoeaT1rXqtWrXLVq1f3257We14lmn+qVI5TTjnFbdiwIdt3Jno/Ou2//vUv995778Ue69Chg7vtttuSlkWfR/i56rN+5JFH/LaYaP6hzz//3F199dVJy52bRGW59NJL/X4ier979+65zgvIBCWCRHvHFKxbt85VqVLFrV271lWuXLnABSnITie/9KUfMGCAmzVrVq7TKjCceeaZrm/fvoVe3ujOKF3L0TxTmVeyHWGy18e/LrdpdeDVjnP58uW5limv8y+OEq33/HxeeV0vCgjPP/98ytNnynpPdXtO53zy+91IRKFaYVu34ckOnD/50Hr5o8WpbkfFGju1LCX/WOkqzp+c57KEryvoZxuui8LYRlI9fmdEE0Nh7HR01h7vkEMOMctVOChdurTr0aOHe+KJJ9y+++4be75Jkybuueeec/369fMr8ZlnnnGjRo1Ke3l1NhhfruhtKFq2qE6dOuW6jFTLnNN0ub0++nwq0w4aNMg1btzYjRw50r322mt5KlemHKTSKf495efzSuU1LVq0cMOHD/e3olqF008/PV9l3JlSKcu5556blvnkNm0q86hRI/sBRjt+INPt9IAQ/+VSStefqmbj6QCdKlXtx7v99tv9vKPV+qKqWn1h99hjD/ftt9+6qlWr+oCxaNEiV6FCBV8lOmnSJFetWrWEZdBze+65pw8a+bFx40b31ltv+aaD0J133pmtSUTlVjiJNheIXrNs2TIzT02n1yQLD3o+upycPpPozqxjx46xz0h/uh+dLlqVq+rg6LS6Hypbtqz/PFq2bJmtyUM70tq1a7spU6b416hpJ9oEo2aFwqBqaQXEnGgbiMrps1ZTmIJPKuKnC9e7mhXiqXlG6yNaXR06+eSTc/we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+Nt169bldxYAAKCIhcft8Die9oCwfv16f1uvXr38zgIAAOwkOo5XqVIlx+dLBLlFiBzs2LHDLV261O22226uRIkSLlNTkgLMTz/95CpXruyKk+Ja9uJabqHsRa+4llsoe9ErruXOtLLrsK9wsNdee7mSJUumvwZBM61bt64rDvRh7OwP5K9W9uJabqHsRa+4llsoe9ErruXOpLInqzkI0UkRAAAYBAQAAPDXCghly5Z1gwYN8rfFTXEte3Ett1D2oldcyy2UvegV13IX17Lnu5MiAADYde3SNQgAACB/CAgAAMAgIAAAAIOAAAAAdn5AGDp0qDvssMP8LzDusccermvXru6bb77JNs3mzZvdZZdd5qpXr+4qVarkunXr5lasWJFtmiuvvNIdcsghvkfogQceaJbzww8/+F94jP/74IMPci3jyJEjXcOGDV25cuXcEUcc4T766KNsZVeZtFz96f/du3ePlS8dZRf1Hb3nnntcs2bN/HR16tRxQ4YMybXskyZNcvvuu68ve6tWrdxrr72WbZ3rxzG03qtWrerXx+eff56x5Y6u89KlS5vP8oQTTigWZVeZypcv75/Xn8r97bffpq3sgwcPTritV6xYMV/benR70Q+61KhRw5dN81yzZk3Gljuk8qvc8fPt27dvbJpMX+8qV+3atV21atX8ewn3Mena1t98803XunVrv6yaNWv6+Wifmen7l3SWO6TyaxvPaf+S6eUXleW8887zv4xYoUKFbPuYAgmKWKdOnYKxY8cGX375ZfD5558HJ510UlC/fv1gw4YNsWn69u0b1KtXL5gyZUrwySefBK1btw7atm2bbT5XXHFF8OCDDwbnnntucMABB5jlLF68WKMzgnfeeSdYtmxZ7G/r1q1Jy/fMM88EZcqUCcaMGRN89dVXwUUXXRRUrVo1WLFihS/7qFGjgrp16wbHHHNM0KFDh6B27drBySefHBx22GHB9u3b01L2cJp99tkneOmll4Lvv//ez+utt95KWvZZs2YFpUqVCu6+++5g/vz5wc033xyULl06aNeuXWyd33777UHTpk2D3Xff3a+fzz77LG3rPN3lnjdvXmx7OfXUU315jj322KBOnTrBokWLgt9//z3jy67taP/99w8OOugg/znstddeQe/evWPbfDrKvn79+mzbuP5atGgR9OrVK1/b+tFHHx3bXvr1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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['DateOS'] = pd.to_datetime(df['DateOS'], errors='coerce')# converts every date stirng to \n",
    "affected_df = df[df['target'] == 1]\n",
    "not_affected_df = df[df['target'] == 0]\n",
    "plot_and_compare_dates(df, affected_df, not_affected_df , 'DateOS')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
