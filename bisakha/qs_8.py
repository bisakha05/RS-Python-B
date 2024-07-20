{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMHMu5WSQLHPBZpcJZFIueD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bisakha05/RS-Python-B/blob/main/bisakha/qs_8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PJv4W8QtYPUw"
      },
      "outputs": [],
      "source": [
        "def count(list):\n",
        " freq={}\n",
        " for i in list:\n",
        "   if i in freq:\n",
        "     freq[i]+=1\n",
        "   else:\n",
        "    freq[i]=1\n",
        " print(freq)\n",
        "list=[4,6,3,7,2,4,5,1,3,6,5]\n",
        "count (list)"
      ]
    }
  ]
}