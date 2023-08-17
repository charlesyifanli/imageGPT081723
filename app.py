{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2aa11d67-cc75-46dc-9177-28df04335438",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import json,time,requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "56853297-5976-49a3-b7a6-4ba295d822bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "79c13d48-5733-44fe-9036-01feb31b3bac",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        q = request.form.get(\"question\")\n",
    "        body = json.dumps(\n",
    "            {\n",
    "                \"version\": \"db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf\", \n",
    "                \"input\": { \"prompt\": q } \n",
    "            }\n",
    "        )\n",
    "        headers = {\n",
    "            \"Authorization\": \"Token r8_DbgnJmLWsgVWHzAMs1MwBDIOTAPgptf2Bz4ds\",\n",
    "            \"Content-Type\": \"application/json\"\n",
    "        }\n",
    "        output = requests.post(\"https://api.replicate.com/v1/predictions\",data=body,headers=headers)\n",
    "        time.sleep(10)\n",
    "        get_url = output.json()['urls']['get']\n",
    "        get_result = requests.post(get_url,headers=headers).json()['output']        \n",
    "        return(render_template(\"index.html\",result=get_result[0]))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "740b35f3-5c15-428e-ad40-c4b8006ce451",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [17/Aug/2023 10:14:21] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:14:21] \"GET /waiting HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:14:42] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:25:53] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:26:13] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:30:26] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:30:49] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:31:14] \"POST / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [17/Aug/2023 10:31:53] \"POST / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adae4723-ab20-45cc-bdf9-429d5c5fd13c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
