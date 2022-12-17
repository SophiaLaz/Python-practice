import unittest
import Task_manager



class Test_task_manager(unittest.TestCase):

    def setUp(self):
        self.taskmanager = TaskManager()
    
    def test_create_task(self):
        result = self.taskmanager.create_task("name", "description")
        expected = {1:Task(1,'name','description','I`m tring my best (in process)')}
        self.assertEqual([result[1].id, result[1].name, result[1].description, result[1].status], 
            [expected[1].id, expected[1].name, expected[1].description, expected[1].status])

    def test_remove_task_by_id(self):
        self.taskmanager.create_task('name1','description1')
        self.taskmanager.create_task('name2','description2')
        self.taskmanager.create_task('name3','description3')
        self.taskmanager.remove_task_by_id(0)
        result = [len(self.taskmanager.tasks), self.taskmanager.tasks[1].name]
        expected = [2, 'name2']
        self.assertEqual(result, expected)
    
    def test_update_status(self):
        self.taskmanager.create_task('name','description')
        self.taskmanager.update_status(self.taskmanager.tasks[1])
        result = self.taskmanager.tasks[1].status
        expected = 'All done, sir'
        self.assertEqual(result,expected)
        

if __name__ == "__main__":
    unittest.main()
