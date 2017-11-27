"""
Modulo que acomopanha o programa moodyDJ

para fazer import deste modulo, copiam-no para a mesma pasta do moodyDJ
"""
import urllib.request
import urllib.parse
import re


def search(searchkeyword):
    """
    Procura videos no youtube dada uma string e retorna o url do primeiro video encontrado
    """
    query_string = urllib.parse.urlencode({"search_query" : searchkeyword})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    video_url = "http://www.youtube.com/watch?v=" + search_results[0]
    return video_url
