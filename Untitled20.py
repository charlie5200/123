{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOA2bjk1pMZdDPUfBg54R1e",
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
        "<a href=\"https://colab.research.google.com/github/charlie5200/123/blob/main/Untitled20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.image(\"最新發票號碼.jpg\")\n",
        "num=st.text_input('輸入您的發票號碼')\n",
        "ns = '11174120' \n",
        "n1 = '59276913'                        \n",
        "n2 = ['18079936','20591738','64500205']\n",
        "n3 = ['ns','n1','n2']\n",
        "if num == ns: st.write(\"對中 1000 萬元！\")\n",
        "if num == ns: st.image(\"恭喜中獎.jpg\")\n",
        "if num == n1: st.write(\"對中 200 萬元！\")\n",
        "if num == n1: st.image(\"恭喜中獎.jpg\")\n",
        "\n",
        "for i in n2:\n",
        "\n",
        "    if num == i:\n",
        "        st.write(\"對中 20 萬元！\") \n",
        "        st.image(\"恭喜中獎.jpg\")\n",
        "        break\n",
        "    elif num[-7:] == i[-7:]:\n",
        "        st.write(\"對中 4 萬元！\") \n",
        "        st.image(\"恭喜中獎.jpg\")\n",
        "        break\n",
        "    elif num[-6:] == i[-6:]:\n",
        "        st.write(\"對中 1 萬元！\") \n",
        "        st.image(\"恭喜中獎.jpg\")\n",
        "        break\n",
        "    elif num[-5:] == i[-5:]:\n",
        "        st.write(\"對中 4000 元\")  \n",
        "        st.image(\"恭喜中獎.jpg\")\n",
        "        break\n",
        "    elif num[-4:] == i[-4:]:\n",
        "        st.write(\"對中 1000 元！\")  \n",
        "        st.image(\"恭喜中獎.jpg\")\n",
        "        break\n",
        "    elif num[-3:] == i[-3:]:\n",
        "        st.write(\"對中 200 元！\")  \n",
        "        st.image(\"恭喜中獎.jpg\")\n",
        "        break\n"
      ],
      "metadata": {
        "id": "dP2hSgOAxp5k"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}