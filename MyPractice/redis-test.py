from redis import Redis

if __name__ == '__main__':
    try:
        rs = Redis()
    except Exception as e:
        print(e)

    result = rs.set('name','itcast')
    print(result)