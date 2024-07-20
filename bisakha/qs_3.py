{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+blpszswzyN8b8aw6u3Fw",
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
        "<a href=\"https://colab.research.google.com/github/bisakha05/RS-Python-B/blob/main/bisakha/qs_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "g2hcfMa7ABxS"
      },
      "outputs": [],
      "source": [
        "a=[]\n",
        "b=int(input(\"enter no.of element:\"))\n",
        "for i in range(0,b):\n",
        "  c=int(input(\"enter list:\"))\n",
        "  a.append(c)\n",
        "print(a)\n",
        "a[-1]+=1\n",
        "print(a)"
      ]
    }
  ]
}