def test_create_task(test_app):
    response = test_app.post('/tasks/', json={
        'title': 'Test Task',
        'description': 'This is a test task',
        'status': 'todo'
    })
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'Test Task'
    assert data['description'] == 'This is a test task'
    assert data['status'] == 'todo'

def test_get_task_by_id(test_app):
    response = test_app.post('/tasks/', json={
        'title': 'Another Task',
        'description': 'Another test task',
        'status': 'in_progress'
    })
    task_id = response.json()['id']

    response = test_app.get(f'/tasks/{task_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == task_id
    assert data['title'] == 'Another Task'
    assert data['status'] == 'in_progress'

def test_filter_tasks_by_status(test_app):
    test_app.post('/tasks/', json={'title': 'Task 1', 'description': 'Desc 1', 'status': 'todo'})
    test_app.post('/tasks/', json={'title': 'Task 2', 'description': 'Desc 2', 'status': 'done'})
    test_app.post('/tasks/', json={'title': 'Task 3', 'description': 'Desc 3', 'status': 'todo'})

    response = test_app.get('/tasks/?status=todo')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    for task in data:
        assert task['status'] == 'todo'
