class Websites:
    def __init__(self, host, domain, queries=''):
        self.host = host
        self.domain = domain
        self.queries = queries

    def produce(self, ):
        if not self.queries == '':
            query = '&'.join([f'[{x}]' for x in self.queries.split(',')])
            return f'https://www.{self.host}.{self.domain}/query?={query}'
        else:
            return f'https://www.{self.host}.{self.domain}'


for token in [x.split(' | ') for x in iter(input, 'end')]:
    if len(token) == 2:
        h, d = token
        web = Websites(h, d)
    else:
        h, d, q = token
        web = Websites(h, d, q)
    print(web.produce())

'''
input:
softuni | bg | user,course,homework
judge.softuni | bg | contest,bg
google | bg | search,query
zamunda | net
end

output:
https://www.softuni.bg/query?=[user]&[course]&[homework]
https://www.judge.softuni.bg/query?=[contest]&[bg]
https://www.google.bg/query?=[search]&[query]
https://www.zamunda.net

'''
