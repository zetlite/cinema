# cinema
with errors
Request Method: POST
Request URL: http://127.0.0.1:800...films/film/add/

Django Version: 2.1
Python Version: 3.7.0
Installed Applications:
['django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'films',
'kinouser',
'otziv',
'guest_otziv']
Installed Middleware:
['django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware']



Traceback:

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\handlers\exception.py" in inner
34. response = get_response(request)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\handlers\base.py" in _get_response
126. response = self.process_exception_by_middleware(e, request)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\handlers\base.py" in _get_response
124. response = wrapped_callback(request, *callback_args, **callback_kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\contrib\admin\options.py" in wrapper
607. return self.admin_site.admin_view(view)(*args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\utils\decorators.py" in _wrapped_view
142. response = view_func(request, *args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\views\decorators\cache.py" in _wrapped_view_func
44. response = view_func(request, *args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\contrib\admin\sites.py" in inner
223. return view(request, *args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\contrib\admin\options.py" in add_view
1647. return self.changeform_view(request, None, form_url, extra_context)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\utils\decorators.py" in _wrapper
45. return bound_method(*args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\utils\decorators.py" in _wrapped_view
142. response = view_func(request, *args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\contrib\admin\options.py" in changeform_view
1536. return self._changeform_view(request, object_id, form_url, extra_context)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\contrib\admin\options.py" in _changeform_view
1575. self.save_model(request, new_object, form, not add)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\contrib\admin\options.py" in save_model
1094. obj.save()

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\base.py" in save
717. force_update=force_update, update_fields=update_fields)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\base.py" in save_base
747. updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\base.py" in _save_table
830. result = self._do_insert(cls._base_manager, using, fields, update_pk, raw)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\base.py" in _do_insert
868. using=using, raw=raw)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\manager.py" in manager_method
82. return getattr(self.get_queryset(), name)(*args, **kwargs)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\query.py" in _insert
1133. return query.get_compiler(using=using).execute_sql(return_id)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\sql\compiler.py" in execute_sql
1284. for sql, params in self.as_sql():

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\sql\compiler.py" in as_sql
1237. for obj in self.query.objs

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\sql\compiler.py" in 
1237. for obj in self.query.objs

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\sql\compiler.py" in 
1236. [self.prepare_value(field, self.pre_save_val(field, obj)) for field in fields]

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\sql\compiler.py" in pre_save_val
1188. return field.pre_save(obj, add=True)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\fields\files.py" in pre_save
288. file.save(file.name, file.file, save=False)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\db\models\fields\files.py" in save
87. self.name = self.storage.save(name, content, max_length=self.field.max_length)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\files\storage.py" in save
48. name = self.get_available_name(name, max_length=max_length)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\files\storage.py" in get_available_name
72. while self.exists(name) or (max_length and len(name) > max_length):

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\files\storage.py" in exists
308. return os.path.exists(self.path(name))

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\files\storage.py" in path
321. return safe_join(self.location, name)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\utils\functional.py" in __get__
37. res = instance.__dict__[self.name] = self.func(instance)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\site-packages\django\core\files\storage.py" in location
201. return os.path.abspath(self.base_location)

File "C:\Users\ZetLite\AppData\Local\Programs\Python\Python37-32\lib\ntpath.py" in abspath
521. path = os.fspath(path)

Exception Type: TypeError at /admin/films/film/add/
Exception Value: expected str, bytes or os.PathLike object, not list
