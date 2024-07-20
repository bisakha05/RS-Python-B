{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPOvCaPw0GzapaKtncEFiSI",
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
        "<a href=\"https://colab.research.google.com/github/bisakha05/RS-Python-B/blob/main/bisakha/qs_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JRvx-Ctd7wxS"
      },
      "outputs": [],
      "source": [
        "a=input(\"enter a string:\")\n",
        "a=a.replace(\"  \",\")\")\n",
        "b=\" \"\n",
        "for i in a:\n",
        "  if i not in b:\n",
        "    b=b+i\n",
        "c=sorted(b)\n",
        "for i in c:\n",
        " print (i,\"->\",a.count(i) )\n",
        "\n"
      ]
    }
  ]
}