# Flask Routes: Deliverables

### 1. Create `GET` `/productions`
#### 1a. Write the query to database
#### 1b. Convert query to a dictionary
#### 1c. Return result with `make_respone`
#### 1d. Test in Postman

<br />

---

<br />

### 2. Create `GET` `/productions/:id`

<br />

---

<br />

### 3. Create `POST` `/productions`
#### 3a. Get information from request using `.get_json()`
#### 3b. Create a new object
#### 3c. Add and commit to `db`
#### 3d. Convert to dictionary
#### 3e. Return as JSON
#### 3f. Test in Postman

<br />

---

<br />

### 4. Create `DELETE` `/productions/:id`

<br />

---

<br />

### 5. Explore Serializers
#### 5a. In `models.py` import `SerializerMixin`
#### 5b. Pass `SerializerMixin` into `Production`
#### 5c. Use `to_dict()` for all responses

<br />

---

<br />

### 6. In `models.py` add a `serialize_rules` to `Production` to remove `updated_at` and `created_at`

<br />

---

<br />

### 7. Create a `Role` table in `models.py`
#### 7a. Create `Role` with `role_name`, `production_id`
#### 7b. Create the relationship between `Role` and `Production`
#### 7c. Uncomment `Role` seeds in `seed.py`
#### 7d. Migrate and seed database
#### 7e. Check `/productions` route

<br />

---

<br />

### 8. Add to `serializer_rules` in `models.py` to avoid max-recursion
#### 8a. Add to `Production`
#### 8b. Add to `Role`

