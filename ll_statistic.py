#!/usr/bin/env python3 -u
import urllib.request, http.cookiejar, json
from sys import exit

class Statistic:
    def __init__(self, method):
        self.method = method

    def get_data(self, ll_url, ll_username, ll_password, start_time, end_time):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        url = 'https://' + ll_url + '/papi/login.xml'
        data = bytes('username=' + ll_username + '&password=' + ll_password, 'utf-8')
        req = urllib.request.Request(url=url,data=data)
        f = opener.open(req)
        if self.method == 'download':
            self.method_url = 'https://' + ll_url + '/papi/net/file/downloads.json?' + 'start_time=' + start_time + '&end_time=' + end_time + '&min_score=70'
        elif self.method == 'mail':
            url = 'https://user.lastline.com/ll_api/ll_api.php?func=get_keys'
            req = urllib.request.Request(url=url)
            f = opener.open(req)
            result = f.read().decode('utf-8')
            decodejson = json.loads(result)
            if decodejson['success'] != 1:   # must equal 1 (int)
                exit('!!! Authentication Failed !!!')
            else:
                key_id = decodejson['data'][0]['access_key_id']
            self.method_url = 'https://' + ll_url + '/ll_api/ll_api.php?func=query_attached_files&start_time=' + start_time + '&end_time=' + end_time + '&key_id=' + key_id + '&min_score=70'
        else:
            exit('!!! Unknown Method !!!')
        req = urllib.request.Request(url=self.method_url)
        f = opener.open(req)
        result = f.read().decode('utf-8')
        decodejson = json.loads(result)
        if decodejson['success'] != 1:   # must equal 1 (int)
            exit('!!! Authentication Failed !!!')
        else:
            return decodejson['data']
        
    def get_top_data(self, top_n, top_by, data):

        def build_array(item, by_item, base_item):
            for d in data:
                if d[by_item] == base_item:
                    if base_item not in array_of:
                        array_of[base_item] = {}
                        array_of[base_item][item] = [d[item]]
                    else:
                        if item not in array_of[base_item]:
                            array_of[base_item][item] = [d[item]]               
                        else: 
                            if d[item] in array_of[base_item][item]:
                                continue
                            else:
                                array_of[base_item][item].append(d[item])

        list_of = []
        for i in data:
            list_of.append(i[top_by])    
        uniq_of = []
        for i in set(list_of):
            uniq_of.append((i,list_of.count(i)))
        uniq_of = sorted(uniq_of, key=lambda uniq: uniq[1], reverse=True)
        if top_n < len(uniq_of):
            uniq_of = uniq_of[:top_n]
        array_of = {}
        if self.method == 'download':        
            if top_by == 'md5':
                info_list = ['score', 'src_host', 'dst_host', 'application_protocol', 'file_name', 'extracted_filename', 'content_disposition_filename', 'llfiletype', 'file_type']
            elif top_by == 'src_host':
                info_list = ['dst_host', 'application_protocol', 'file_name', 'extracted_filename', 'content_disposition_filename', 'llfiletype', 'file_type']
            elif top_by == 'dst_host':
                info_list = ['src_host', 'application_protocol', 'file_name', 'extracted_filename', 'content_disposition_filename', 'llfiletype', 'file_type']
        elif self.method == 'mail':
            if top_by == 'md5':
                info_list = ['score', 'sender', 'recipient', 'subject', 'file_name', 'llfiletype', 'file_type']
            elif top_by == 'sender':
                info_list = ['recipient', 'subject', 'file_name', 'md5', 'llfiletype', 'file_type']
            elif top_by == 'recipient':
                info_list = ['sender', 'subject', 'file_name', 'md5', 'llfiletype', 'file_type']
            elif top_by == 'subject':
                info_list = ['sender', 'recipient', 'md5', 'file_name', 'llfiletype', 'file_type']                
        else:
            exit('!!! Unknown Method !!!')        
        for i, t in uniq_of:
            print('-' * 50)
            print(i + ':')
            print('\t' + 'Times: ' + str(t))
            for j in info_list:
                build_array(j, top_by, i)
                print('\t' + j + ': ' + str(array_of[i][j]))

def main():
    ll_url = 'user.lastline.com'
    ll_username = 'abc@demo.com'
    ll_password = 'passw0rd'
    start_time = '2014-12-16'
    end_time = '2015-03-15'
    s = Statistic('mail')   # can be 'mail' or 'download'
    data = s.get_data(ll_url, ll_username, ll_password, start_time, end_time)
    top_n = 3
    '''
    if 'download': 'md5', 'src_host', 'dst_host'
    if 'mail': 'md5', 'sender', 'recipient' , 'subject'
    '''
    top_by = 'md5'
    s.get_top_data(top_n, top_by, data)
    
if __name__ == '__main__':
    main()
