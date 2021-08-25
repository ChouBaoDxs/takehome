---
title: django-ocr v1.0.0

---

# django-ocr

> v1.0.0

# ocr_record

## GET Ocr 解析记录-单个

GET /api/ocr_record/{id}/

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|path|string|true|none|

> 返回示例

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[OcrRecordDisplaySer](#schemaocrrecorddisplayser)|

## GET Ocr 解析记录-列表

GET /api/ocr_record/

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|query|string|false|none|
|image_md5|query|string|false|none|
|image_size__lte|query|string|false|none|
|image_size__gte|query|string|false|none|
|created_at__lte|query|string|false|none|
|created_at__gte|query|string|false|none|
|search|query|string|false|A search term.|
|ordering|query|string|false|Which field to use when ordering the results.|
|page|query|string|false|A page number within the paginated result set.|
|page_size|query|string|false|Number of results to return per page.|

> 返回示例

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)¦null|false|none|none|
|» previous|string(uri)¦null|false|none|none|
|» results|[[OcrRecordDisplaySer](#schemaocrrecorddisplayser)]|true|none|none|
|»» id|integer|false|read-only|none|
|»» created_at|string(date-time)|false|read-only|none|
|»» image_md5|string|true|none|长度为 32 的小写字母、数字|
|»» image_size|integer|true|none|单位为 B|
|»» content|[string]|true|none|识别结果|

## POST 解析图片中的字母

POST /api/ocr_record/parse_letter/

> Body 请求参数

```yaml
type: object
properties:
  image:
    type: string
    format: binary
required:
  - image

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object|false|none|
|» image|body|string(binary)|true|none|

> 返回示例

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|[OcrParseLetterResSer](#schemaocrparseletterresser)|

# 数据模型

<h2 id="tocS_OcrParseLetterResSer">OcrParseLetterResSer</h2>
<!-- backwards compatibility -->
<a id="schemaocrparseletterresser"></a>
<a id="schema_OcrParseLetterResSer"></a>
<a id="tocSocrparseletterresser"></a>
<a id="tocsocrparseletterresser"></a>

```json
{
  "required": [
    "content"
  ],
  "type": "object",
  "properties": {
    "content": {
      "description": "解析图片得到的字母列表",
      "type": "array",
      "items": {
        "description": "字母",
        "type": "string",
        "maxLength": 1,
        "minLength": 1
      }
    }
  }
}

```

### 属性

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|content|[string]|true|none|解析图片得到的字母列表|

<h2 id="tocS_OcrRecordDisplaySer">OcrRecordDisplaySer</h2>
<!-- backwards compatibility -->
<a id="schemaocrrecorddisplayser"></a>
<a id="schema_OcrRecordDisplaySer"></a>
<a id="tocSocrrecorddisplayser"></a>
<a id="tocsocrrecorddisplayser"></a>

```json
{
  "required": [
    "image_md5",
    "image_size",
    "content"
  ],
  "type": "object",
  "properties": {
    "id": {
      "title": "Id",
      "type": "integer",
      "readOnly": true
    },
    "created_at": {
      "title": "创建时间",
      "type": "string",
      "format": "date-time",
      "readOnly": true
    },
    "image_md5": {
      "title": "图片的md5",
      "description": "长度为 32 的小写字母、数字",
      "type": "string",
      "maxLength": 32,
      "minLength": 1
    },
    "image_size": {
      "title": "图片的大小",
      "description": "单位为 B",
      "type": "integer"
    },
    "content": {
      "description": "识别结果",
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    }
  }
}

```

### 属性

|名称|类型|必选|约束|说明|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|created_at|string(date-time)|false|read-only|none|
|image_md5|string|true|none|长度为 32 的小写字母、数字|
|image_size|integer|true|none|单位为 B|
|content|[string]|true|none|识别结果|

