## Formik errors

```js
{formik.touched.field && formik.errors.field ? <h3>{formik.errors.field}</h3> : ''}
```

<strong>Note:</strong> you need to have an onblur event in order for `formik.touched` to get populated 

```js
<label>Field</label>
<input
    type="number"
    name="field"
    value={formik.values.field}
    onChange={formik.handleChange}
    onBlur={formik.handleBlur}
/>
```