import pymysql
import time
import requests
from collections import namedtuple

_CONN = pymysql.connect(host='127.0.0.1',
                       user='root',
                       passwd='cashme0304mush',
                       db='testdouyu',
                       charset='utf8'
                      )

def get_info_by_rid(roomid):
    url = 'http://open.douyucdn.cn/api/RoomApi/room/%s' % roomid
    i_tag = 0
    while True:
        try:
            msg_dict = requests.get(url).json()
        except Exception as e:
            print('request error in {}/10'.format(i_tag), e)
            if i_tag == 10:
                print('rid request error')
                return False
            time.sleep(10)
            i_tag += 1
        else:
            break
    if msg_dict['error'] == 0:
        return msg_dict
    return dict()

def get_info_by_file(path = '/home/hikaru/Downloads/giftmsg520'):
    with open(path, 'r') as f:
        for line in f:
            info = eval(line)
            assert type(info) is dict, 'not a dict'
            yield info
        return

def info_to_sql(info: dict):
    cursor = _CONN.cursor(cursor=pymysql.cursors.DictCursor)
    Gift = namedtuple('Gift',
                      'gid giftname gifttype contrib mimg himg desc intro')
    data = info.get('data')
    if data:
        gifts = data.get('gift')
        if gifts:
            giftList = list()
            for giftdict in gifts:
                gfid = giftdict.get('id')
                if is_exists(gfid):
                    continue
                gift = Gift(int(giftdict['id']), giftdict['name'],
                            int(giftdict['type']), int(giftdict['gx']),
                            giftdict['mimg'], giftdict['himg'],
                            giftdict['desc'], giftdict['intro'])
                giftList.append(gift)
            if giftList:
                sql = """
                INSERT INTO gift
                (`gid`, `giftname`, `gifttype`, `contrib`, `mimg`, `himg`, `desc`, `intro`)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.executemany(sql, giftList)
                _CONN.commit()
                cursor.close()

def is_exists(gfid):
    cursor = _CONN.cursor(cursor=pymysql.cursors.DictCursor)
    sql = """
    SELECT gid
    FROM gift
    WHERE gid = %s;
    """
    cursor.execute(sql, gfid)
    if cursor.fetchone()['giftname']:
        return True
    else:
        return False

if __name__ == '__main__':
    infoes = get_info_by_file()
    for info in infoes:
        info_to_sql(info)
