from InstagramScrapper import loginInstagram
from InstagramScrapper import searchUserFollowersFollowings
from InstagramScrapper import getFollowersFrom

from myLibs import writeListToFile

username = ""
password = ""
searchUser = ""
mode = "followings"

# browser1 = loginInstagram(username, password)
# lst = searchUserFollowersFollowings(searchUser, mode, browser1)
# writeListToFile(lst, searchUser + "_" + mode)

getFollowersFrom(username, password, username, "buddy140", "pofol")
