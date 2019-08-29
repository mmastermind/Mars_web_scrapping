{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import time\n",
    "\n",
    "\n",
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"/usr/local/bin/chromedriver\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)\n",
    "\n",
    "\n",
    "def scrape_info():\n",
    "    browser = init_browser()\n",
    "\n",
    "    # Visit mars.nasa.gov/news\n",
    "    url = \"https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    time.sleep(1)\n",
    "\n",
    "    # Scrape page into Soup\n",
    "    html = browser.html\n",
    "    soup = bs(html, \"html.parser\")\n",
    "    \n",
    "    news_titles = soup.findAll('div', {\"class\":'content_title'}).get_text(strip=True)\n",
    "    \n",
    "    # Get the min avg temp\n",
    "    #min_temp = avg_temps.find_all('strong')[0].text\n",
    "\n",
    "    # Get the max avg temp\n",
    "    #max_temp = avg_temps.find_all('strong')[1].text\n",
    "\n",
    "    return news_titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-3-eacec1d107fa>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-eacec1d107fa>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    news_titles = soup.find('div', class='content_title')\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# Get the news titles\n",
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
    "\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # BONUS: Find the src for the sloth image\n",
    "    relative_image_path = soup.find_all('img')[2][\"src\"]\n",
    "    sloth_img = url + relative_image_path\n",
    "\n",
    "    # Store data in a dictionary\n",
    "    costa_data = {\n",
    "        \"sloth_img\": sloth_img,\n",
    "        \"min_temp\": min_temp,\n",
    "        \"max_temp\": max_temp\n",
    "    }\n",
    "\n",
    "    # Close the browser after scraping\n",
    "    browser.quit()\n",
    "\n",
    "    # Return results\n",
    "    return costa_data\n"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
