#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install splinter


# In[2]:


pip install webdriver_manager


# In[3]:


pip install bs4


# In[4]:


# Import Splinter and BeautifulSoup
import pandas as pd 
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[5]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[7]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[8]:


slide_elem.find('div', class_= 'content_title')


# In[9]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[11]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[14]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[15]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[16]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[18]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[20]:


df.to_html()


# In[25]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[26]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[28]:


#parse 
html = browser.html
#hemi_soup = soup(html, 'htm.parser')


# In[29]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemi_soup(html, 'html.parser')
# 3. Write code to retrieve the image urls and titles for each hemisphere.
hemi_iteams =  hemi_soup.find_all('div', class_ = 'item')


# In[30]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[31]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[32]:


slide_elem.find('div', class_='content_title')


# In[33]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[34]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[35]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[36]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[37]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[38]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel




# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[40]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[41]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[42]:


df.to_html()




# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[ ]:


#parse 
html = browser.html
hemi_soup = soup(html, 'htm.parser')


# In[ ]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemi_soup(html, 'html.parser')
# 3. Write code to retrieve the image urls and titles for each hemisphere.
hemi_iteams = hemi_soup.find_all('div', class_ = 'iteam')


# In[43]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls = []




for x in hemi_iteams : 
    #create an empty dict 
    hemispheres = {}
    
    #find image url 
    main_url = x.find('a',class_ ='itemLink')['href']
    browser.visit(url + '/' + main_url )
    
    main_url = brownser.html
    image_soup = soup(main_url,'html.parser')
    hemi_url = url + image_soup('ing', class_ ='wide-image')[0]['src']
    
    #find title 
    hemi_title = x.find('h3').text 
    
    #store in dictionary 
    hemisphere['img_url'] = hemi_url
    hemisphere['title'] = hemo_title 


# 



# 5. Quit the browser
browser.quit()

