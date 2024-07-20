{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNCmoiwPV0ypVM8U2A1RnuG",
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
        "<a href=\"https://colab.research.google.com/github/bisakha05/RS-Python-B/blob/main/bisakha/qs_6.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "z3rIsHwbPxrB"
      },
      "outputs": [],
      "source": [
        "N=int(input(\"enter the no. of elements:\"))\n",
        "A=[]\n",
        "min=0\n",
        "max=0\n",
        "for i in range (N):\n",
        "  x=int(input(\"enter the element:\"))\n",
        "  A.append(x)\n",
        "b=sorted(A)\n",
        "for i in range(N):\n",
        "   if isPrime(b[i]):\n",
        "    min=b[i]\n",
        "    break\n",
        "for i in range(N-1,0,-1):\n",
        "   if isPrime(b[i]):\n",
        "     max=b[i]\n",
        "if max==min and max!=0 and min!=0:\n",
        "  print(\"difference=\",max-min)\n",
        "else:\n",
        "  print (\"difference=\",min)\n",
        "if max==min and max==0:\n",
        "  print(1)"
      ]
    }
  ]
}