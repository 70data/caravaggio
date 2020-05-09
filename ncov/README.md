# ncov

### status

path: /api/mark/status

method: GET

request:
```json

```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": {}
}
```

### 用户注册

path: /api/mark/user/register

method: POST

request:
```json
{
	"phone": "17090079838",
	"password": "123456"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 用户登陆

path: /api/mark/user/login

method: POST

request:
```json
{
	"phone": "17090079838",
	"password": "123456"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": [
        {
            "id": 35,
            "phone": "17090079838",
            "password": "e10adc3949ba59abbe56e057f20f883e",
            "region_info": [
                {
                    "id": 6210,
                    "pid": 6209,
                    "level": 2,
                    "name": "沈阳市"
                },
                {
                    "id": 6756,
                    "pid": 6209,
                    "level": 2,
                    "name": "抚顺市"
                }
            ],
            "token": "5eedba3c-eb6a-4f26-8b20-e599056d87df",
            "admin": 1
        }
    ]
}
```

### 用户信息查询

path: /api/mark/user/info

method: POST

request:
```json
{
	"phone": "17090079838"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": [
        {
            "id": 35,
            "phone": "17090079838",
            "password": "e10adc3949ba59abbe56e057f20f883e",
            "region_info": [
                {
                    "id": 6210,
                    "pid": 6209,
                    "level": 2,
                    "name": "沈阳市"
                },
                {
                    "id": 6756,
                    "pid": 6209,
                    "level": 2,
                    "name": "抚顺市"
                }
            ],
            "token": "5eedba3c-eb6a-4f26-8b20-e599056d87df",
            "admin": 1
        }
    ]
}
```

### 用户信息更新

path: /api/mark/user/update

method: POST

request:
```json
{
	"phone": "17090079838",
	"region_id": [6209,6210,6211]
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 统计信息插入

path: /api/mark/count/insert

method: POST

request:
```json
{
	"countRegionId": 6211,
	"countDate": "2020-02-10",
	"countConfirm": 1,
	"countRecover": 1,
	"countDead": 1,
	"countSourceUrl": "www.so.com",
	"countSourceText": "测试"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 统计信息更新

path: /api/mark/count/update

method: POST

request:
```json
{
	"id": 14,
	"countRegionId": 1,
	"countDate": "2020-02-05",
	"countConfirm": 1,
	"countRecover": 1,
	"countDead": 1,
	"countSourceUrl": "www.so.com",
	"countSourceText": "测试1"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 统计信息删除

path: /api/mark/count/delete

method: POST

request:
```json
{
	"countId": 14
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 统计信息获取

path: /api/mark/info/getCount

method: POST

request:
```json
{
	"locId": 11,
	"date": "2020-02-05"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": [
        {
            "id": 13,
            "countConfirm": 1,
            "countRecover": 1,
            "countDead": 1,
            "countSourceUrl": "www.so.com",
            "countSourceText": "测试",
            "countRegionId": 6211,
            "locName": "辽宁省-沈阳市-市辖区"
        }
    ]
}
```

### 病例信息插入

path: /api/mark/sample/insert

method: POST

request:
```json
{
	"sampleRegionId": 6211,
	"sampleType": 1,
	"sampleSex": 1,
	"sampleAge": 18,
	"sampleDate": "2020-02-10",
	"sampleConfirmTime": "2020-02-10",
	"sampleSourceUrl": "www.so.com",
	"sampleSourceText": "测试",
	"sampleCustomTag": [
		{
			"key": "身高",
			"value": "185"
		},
		{
			"key": "职业",
			"value": "学生"
		}
	]
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 病例信息更新

path: /api/mark/sample/update

method: POST

request:
```json
{
	"id": 19,
	"sampleRegionId": 6211,
	"sampleType": 2,
	"sampleSex": 1,
	"sampleAge": 18,
	"sampleDate": "2020-02-10",
	"sampleConfirmTime": "2020-02-10",
	"sampleSourceUrl": "www.so.com",
	"sampleSourceText": "测试1",
	"sampleCustomTag": [
		{
			"key": "身高",
			"value": "1851"
		},
		{
			"key": "职业",
			"value": "学生1"
		}
	]
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 病例信息删除

path: /api/mark/sample/delete

method: POST

request:
```json
{
	"patId": 19
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```

### 病例信息获取

path: /api/mark/info/getPat

method: POST

request:
```json
{
	"locId": 6210,
	"date": "2020-02-10"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": [
        {
            "id": 18,
            "sampleRegionId": 6211,
            "sampleConfirmTime": "2020-02-10",
            "sampleType": 1,
            "sampleSex": 1,
            "sampleAge": 18,
            "sampleSourceText": "测试",
            "sampleSourceUrl": "www.so.com",
            "sampleCustomTag": [
                {
                    "key": "身高",
                    "value": "185"
                },
                {
                    "key": "职业",
                    "value": "学生"
                }
            ],
            "locName": "辽宁省-沈阳市-市辖区"
        }
    ]
}
```

### 获取下级地区

path: /api/mark/info/getNextLoc

method: POST

request:
```json
{
	"locId": 2
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": [
        {
            "id": 3,
            "level": 3,
            "name": "东城区"
        }
    ]
}
```

### 新增子地区

path: /api/mark/region/insert

method: POST

request:
```json
{
	"partnerId": 6209,
	"level": 3,
	"name": "测试"
}
```

response:
```json
{
    "status": 0,
    "desc": "succeed",
    "data": []
}
```
