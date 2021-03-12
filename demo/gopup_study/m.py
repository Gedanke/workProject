# -*- coding:utf-8 -*-

import gopup


def gain_weibo_msg():
    """
    微博指数
    :return:
    """
    weibo_index = gopup.weibo_index(word="CSGO", time_type="1month")
    """
    weibo_index:
    :param word: str
    :param time_type: str 1hour, 1day, 1month, 3month
    """
    print(weibo_index)


def gain_baidu_msg():
    """
    百度指数
    :return:
    """
    cookie = "输入网页端登录百度指数后的cookie"
    baidu_index = gopup.baidu_search_index(word="CSGO", start_date='2021-2-26', end_date='2021-2-27', cookie=cookie)
    print(baidu_index)


def gain_toutiao_msg():
    """
    头条指数
    :return:
    """
    toutiao_index = gopup.toutiao_index(keyword="CSGO", start_date='20201115', end_date='20201125')
    print(toutiao_index)


def gain_google_msg():
    """
    谷歌数据
    :return:
    """
    google_data = gopup.google_index(keyword="CSGO", start_date='2020-11-15', end_date='2020-11-25')
    print(google_data)


def gain_marco_cmlrd():
    """
    宏观经济数据
    :return:
    """
    marco_cmlrd_data = gopup.marco_cmlrd()
    '''problem?'''
    print(marco_cmlrd_data)


def gain_nicorn_company():
    """
    独角兽公司数据
    :return:
    """
    nicorn_company_data = gopup.nicorn_company()
    print(nicorn_company_data)


def gain_death_company():
    """
    倒闭公司数据
    :return:
    """
    death_company_data = gopup.death_company()
    print(death_company_data)


def gain_pro_api():
    """
    KOL 数据
    :return:
    """
    """
    第一次可以通过gp.set_token('your token')来记录自己的token凭证，
    临时token可以通过本参数传入
    """
    g = gopup.pro_api(token="c9a86581437bcdff318e53fc23a28356")
    weibo_user_data = g.weibo_user(keyword="雷军")
    print(weibo_user_data)


def gain_energy_oil_hist():
    """
    油价数据
    :return:
    """
    energy_oil_hist_data = gopup.energy_oil_hist()
    print(energy_oil_hist_data)


def gain_migration_area_baidu():
    """
    迁徙数据
    :return:
    """
    """
    some param:
    :param indicator: move_in 迁入 move_out 迁出
    """
    migration_area_baidu_data = gopup.migration_area_baidu(area="湖北省", indicator="move_in", date="20210201")
    print(migration_area_baidu_data)


def gain_realtime_boxoffice():
    """
    实时电影票房数据
    :return:
    """
    realtime_boxoffice_data = gopup.realtime_boxoffice()
    print(realtime_boxoffice_data)


def gain_day_cinema():
    """
    单日影院数据
    :return:
    """
    day_cinema_data = gopup.day_cinema(date="2021-2-26")
    print(day_cinema_data)


def gain_realtime_tv():
    """
    电视剧数据
    :return:
    """
    realtime_tv_data = gopup.realtime_tv()
    print(realtime_tv_data)


def gain_university():
    """

    :return:
    """
    university_data = gopup.university()
    print(university_data)


def gain_covid():
    """
    世界历史累计确诊数据
    :return:
    """
    covid_163_data = gopup.covid_163(indicator="世界历史累计数据")
    print(covid_163_data)


if __name__ == '__main__':
    """https://github.com/justinzm/gopup"""
    # gain_weibo_msg()
    # gain_baidu_msg()
    # gain_toutiao_msg()
    # gain_google_msg()
    # gain_marco_cmlrd()
    # gain_nicorn_company()
    # gain_death_company()
    # gain_pro_api()
    # gain_energy_oil_hist()
    # gain_migration_area_baidu()
    # gain_realtime_boxoffice()
    # gain_day_cinema()
    # gain_realtime_tv()
    # gain_university()
    # gain_covid()
