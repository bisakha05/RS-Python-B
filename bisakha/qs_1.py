{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOWni5iCR5MSoShXEjtAaMs",
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
        "<a href=\"https://colab.research.google.com/github/bisakha05/RS-Python-B/blob/main/bisakha/qs_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3R3aQ2UJ0EIs"
      },
      "outputs": [],
      "source": [
        "s=input('enter 1st string')\n",
        "t=input('enter 2nd string')\n",
        "if(len(s)==len(t)):\n",
        "  if(sorted(t)==sorted(s)):\n",
        "    print ('true')\n",
        "  else:\n",
        "    print('false')\n",
        "else:\n",
        "  print('false')\n"
      ]
    }
  ]
}