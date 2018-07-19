# PUBG-data
![banner1](https://github.com/sarimzk/PUBG-data/blob/master/banner.png)  
  
A scrape of dak.gg, which is a PUBG (PlayerUnknown's Battlegrounds) leaderboard website, to gather player statistics and explore the generated dataset

## Scraping The Data
The goal is to scrape the data for the top 100 solo-FPP players of the 2018-06 season. A list of top 100 solo-FPP players is available at this link: https://dak.gg/ranks/na/solo-fpp/rating  
   
We will be using Selenium along with PhantomJS for accessing the webpages and BeautifulSoup for parsing the HTML data.  
  
First, we visit this link and gather the url for each of the top 100 players' profile page and store them in a list. Then, we visit each link and gather the individual player stats from them, storing them in a list called stats. Finally, we use the csv module to write the files to the storage as a csv (comma separated values) file.  
  
This can be done by executing the python script *player names.py*. Upon execution, it will create a new csv file called *output.csv*, that will contain all the collected statistics for the top hundred players.

<div class='tableauPlaceholder' id='viz1531994547244' style='position: relative'>
  <noscript>  
    <a href='#'>
       <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Na&#47;Names_32&#47;Dashboard1&#47;1_rss.png' style='border: none' />
    </a>
  </noscript>
  <object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
    <param name='embed_code_version' value='3' /> 
    <param name='site_root' value='' />
    <param name='name' value='Names_32&#47;Dashboard1' />
    <param name='tabs' value='yes' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Na&#47;Names_32&#47;Dashboard1&#47;1.png' /> 
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='filter' value='publish=yes' />
  </object>
</div>                

<script type='text/javascript'>                    
  var divElement = document.getElementById('viz1531994547244');                    
  var vizElement = divElement.getElementsByTagName('object')[0];                         
  vizElement.style.width='100%';
  vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    
  var scriptElement = document.createElement('script');                    
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
