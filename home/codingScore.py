# import json
# import re
# # DO NOT import this after requests
# import grequests
# import requests
# import os

# from bs4 import BeautifulSoup
# # from selenium import webdriver
# # from selenium.webdriver.common.action_chains import ActionChains


# class UsernameError(Exception):
#     pass


# class PlatformError(Exception):
#     pass


# class UserData:
#     def __init__(self, username=None):
#         self.__username = username

#     def update_username(self, username):
#         self.__username = username

#     def __codechef(self):
#         url = 'https://www.codechef.com/users/{}'.format(self.__username)

#         page = requests.get(url)

#         soup = BeautifulSoup(page.text, 'html.parser')

#         try:
#             rating = soup.find('div', class_='rating-number').text
#         except AttributeError:
#             return {"rating" : "Not Valid" , "psolved": "Not exist" ,"fsolved":"Not available"}

#         stars = soup.find('span', class_='rating')
#         if stars:
#             stars = stars.text

#         highest_rating_container = soup.find('div', class_='rating-header')
#         highest_rating = highest_rating_container.find_next('small').text.split()[-1].rstrip(')')

#         rating_ranks_container = soup.find('div', class_='rating-ranks')
#         rating_ranks = rating_ranks_container.find_all('a')

#         global_rank = rating_ranks[0].strong.text
#         country_rank = rating_ranks[1].strong.text

#         if global_rank != 'NA':
#             global_rank = int(global_rank)
#             country_rank = int(country_rank)

#         def contests_details_get():
#             rating_table = soup.find('table', class_='rating-table')

#             rating_table_rows = rating_table.find_all('td')

#             '''Can add ranking url to contests'''

#             try:
#                 long_challenge = {'name': 'Long Challenge', 'rating': int(rating_table_rows[1].text),
#                                   'global_rank': int(rating_table_rows[2].a.hx.text),
#                                   'country_rank': int(rating_table_rows[3].a.hx.text)}

#             except ValueError:
#                 long_challenge = {'name': 'Long Challenge', 'rating': int(rating_table_rows[1].text),
#                                   'global_rank': rating_table_rows[2].a.hx.text,
#                                   'country_rank': rating_table_rows[3].a.hx.text}

#             try:
#                 cook_off = {'name': 'Cook-off',
#                             'rating': int(rating_table_rows[5].text),
#                             'global_rank': int(rating_table_rows[6].a.hx.text),
#                             'country_rank': int(rating_table_rows[7].a.hx.text)}
#             except ValueError:
#                 cook_off = {'name': 'Cook-off',
#                             'rating': int(rating_table_rows[5].text),
#                             'global_rank': rating_table_rows[6].a.hx.text,
#                             'country_rank': rating_table_rows[7].a.hx.text}

#             try:
#                 lunch_time = {'name': 'Lunch Time', 'rating': int(rating_table_rows[9].text),
#                               'global_rank': int(rating_table_rows[10].a.hx.text),
#                               'country_rank': int(rating_table_rows[11].a.hx.text)}

#             except ValueError:
#                 lunch_time = {'name': 'Lunch Time', 'rating': int(rating_table_rows[9].text),
#                               'global_rank': rating_table_rows[10].a.hx.text,
#                               'country_rank': rating_table_rows[11].a.hx.text}

#             return [long_challenge, cook_off, lunch_time]

#         def contest_rating_details_get():
#             start_ind = page.text.find('[', page.text.find('all_rating'))
#             end_ind = page.text.find(']', start_ind) + 1

#             next_opening_brack = page.text.find('[', start_ind + 1)
#             while next_opening_brack < end_ind:
#                 end_ind = page.text.find(']', end_ind + 1) + 1
#                 next_opening_brack = page.text.find('[', next_opening_brack + 1)

#             all_rating = json.loads(page.text[start_ind: end_ind])
#             for rating_contest in all_rating:
#                 rating_contest.pop('color')

#             return all_rating

#         def problems_solved_get():
#             problem_solved_section = soup.find('section', class_='rating-data-section problems-solved')

#             no_solved = problem_solved_section.find_all('h5')

#             categories = problem_solved_section.find_all('article')

#             fully_solved = {'count': int(re.findall(r'\d+', no_solved[0].text)[0])}

#             if fully_solved['count'] != 0:
#                 for category in categories[0].find_all('p'):
#                     category_name = category.find('strong').text[:-1]
#                     fully_solved[category_name] = []

#                     for prob in category.find_all('a'):
#                         fully_solved[category_name].append({'name': prob.text,
#                                                             'link': 'https://www.codechef.com' + prob['href']})

#             partially_solved = {'count': int(re.findall(r'\d+', no_solved[1].text)[0])}
#             if partially_solved['count'] != 0:
#                 for category in categories[1].find_all('p'):
#                     category_name = category.find('strong').text[:-1]
#                     partially_solved[category_name] = []

#                     for prob in category.find_all('a'):
#                         partially_solved[category_name].append({'name': prob.text,
#                                                                 'link': 'https://www.codechef.com' + prob['href']})

#             return fully_solved, partially_solved

#         def user_details_get():
#             header_containers = soup.find_all('header')
#             name = header_containers[1].find('h2').text

#             user_details_section = soup.find('section', class_='user-details')
#             user_details_list = user_details_section.find_all('li')

#             return {'name': name, 'username': user_details_list[0].text.split('★')[-1].rstrip('\n'),
#                     'country': user_details_list[1].text.split(':')[-1].strip(),
#                     'state': user_details_list[2].text.split(':')[-1].strip(),
#                     'city': user_details_list[3].text.split(':')[-1].strip(),
#                     'student/professional': user_details_list[4].text.split(':')[-1].strip(),
#                     'institution': user_details_list[5].text.split(':')[-1].strip()}

#         full, partial = problems_solved_get()
#         details = {'status': 'Success', 'rating': int(rating), 'stars': stars, 'highest_rating': int(highest_rating),
#                    'global_rank': global_rank, 'country_rank': country_rank,
#                    'user_details': user_details_get(), 'contests': contests_details_get(),
#                    'contest_ratings': contest_rating_details_get(), 'fully_solved': full, 'partially_solved': partial}

#         return {"rating": details['stars'],"fsolved": details['fully_solved']['count'], "psolved": details['partially_solved']['count']}

#     def __codeforces(self):
#         urls = {
#             "user_info": {"url": f'https://codeforces.com/api/user.info?handles={self.__username}'},
#             "user_contests": {"url": f'https://codeforces.com/contests/with/{self.__username}'}
#         }

#         reqs = [grequests.get(item["url"]) for item in urls.values() if item.get("url")]

#         responses = grequests.map(reqs)

#         details_api = {}
#         contests = []
#         for page in responses:
#             if page.status_code != 200:
#                 return  {"rating" :"Invalid Handle","solved":'N/A'}
#             if page.request.url == urls["user_info"]["url"]:
#                 details_api = page.json()
#             elif page.request.url == urls["user_contests"]["url"]:
#                 soup = BeautifulSoup(page.text, 'html.parser')
#                 table = soup.find('table', attrs={'class': 'user-contests-table'})
#                 table_body = table.find('tbody')

#                 rows = table_body.find_all('tr')
#                 for row in rows:
#                     cols = row.find_all('td')
#                     cols = [ele.text.strip() for ele in cols]
#                     contests.append({
#                         "Contest": cols[1],
#                         "Rank": cols[3],
#                         "Solved": cols[4],
#                         "Rating Change": cols[5],
#                         "New Rating": cols[6]
#                     })

#         if details_api.get('status') != 'OK':
#             return  {"rating" :"Invalid Handle","solved":'N/A'}

#         details_api = details_api['result'][0]

#         try:
#             rating = details_api['rating']
#             max_rating = details_api['maxRating']
#             rank = details_api['rank']
#             max_rank = details_api['maxRank']

#         except KeyError:
#             rating = 'Unrated'
#             max_rating = 'Unrated'
#             rank = 'Unrated'
#             max_rank = 'Unrated'

#         # return {
#         #     'status': 'Success',
#         #     'username': self.__username,
#         #     'platform': 'Codeforces',
#         #     'rating': rating,
#         #     'max rating': max_rating,
#         #     'rank': rank,
#         #     'max rank': max_rank,
#         #     'contests': contests
#         # }
#         solved =0
#         try:
#             for contest in contests:
#                 solved = solved + int(contest['Solved'])
#         except:
#             pass
#         return {
#             'rating': rating,
#             'solved':solved
#         }

#     def __spoj(self):
#         url = 'https://www.spoj.com/users/{}/'.format(self.__username)

#         page = requests.get(url)

#         soup = BeautifulSoup(page.text, 'html.parser')
#         details_container = soup.find_all('p')

#         points = details_container[2].text.split()[3][1:]
#         rank = details_container[2].text.split()[2][1:]
#         join_date = details_container[1].text.split()[1] + ' ' + details_container[1].text.split()[2]
#         institute = ' '.join(details_container[3].text.split()[1:])

#         try:
#             points = float(points)

#         except ValueError:
#             return {'rating':'Invalid Handle','solved':0}

#         def get_solved_problems():
#             table = soup.find('table', class_='table table-condensed')

#             rows = table.findChildren('td')

#             solved_problems = []
#             for row in rows:
#                 if row.a.text:
#                     solved_problems.append(row.a.text)

#             return solved_problems

#         details = {
#                    'rating': float(points),'solved': len(get_solved_problems())
#                    }
#         return details


#     def __interviewbit(self):
#         url = 'https://www.interviewbit.com/profile/{}'.format(self.__username)

#         page = requests.get(url)
#         print(page)
#         if page.status_code != 200:
#             return {'rating': 'Invalid Handle', 'solved':0}

#         soup = BeautifulSoup(page.text, 'html.parser')
#         details_main = soup.find('div', class_='user-stats')
#         details_container = details_main.findChildren('div', recursive=False)
        
#         details = {
#                    'rank': int(details_container[0].find('div', class_='txt').text),
#                    'rating': int(details_container[1].find('div', class_='txt').text),
#                    'streak': details_container[2].find('div', class_='txt').text}

#         return details

    
#     def get_details(self, platform):
#         if platform == 'codechef':
#             return self.__codechef()

#         if platform == 'codeforces':
#             return self.__codeforces()

#         if platform == 'spoj':
#             try:
#                 return self.__spoj()
#             except:
#                 return {'rating': 'Invalid Handle', 'solved':0}

#         if platform == 'interviewbit':
#             return self.__interviewbit()

#         # if platform == 'leetcode':
#         #     return self.__leetcode()

#         raise PlatformError('Platform not Found')


# # if __name__ == '__main__':
# #     ud = UserData('harshguptashnd_92f3015228a2')

# #     ans = ud.get_details('interviewbit')

# #     print(ans)