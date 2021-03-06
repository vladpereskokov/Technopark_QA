# -*- coding: utf-8 -*-

from vp_check_list.tests.base_test import BaseTest


class SimpleAddDeleteCommentsTest(BaseTest):
	TEST_COMMENT = 'Test comment'

	def test_add_comment(self):
		self.user_avatar.open_avatar()
		avatar_footer = self.user_avatar.comments

		avatar_footer.add_comment_to_avatar(self.TEST_COMMENT)

		comment = avatar_footer.last_comment.text()
		self.assertEqual(comment, self.TEST_COMMENT)

	def test_delete_comment(self):
		self.user_avatar.open_avatar()

		avatar_footer = self.user_avatar.comments
		comment_before_delete = avatar_footer.last_comment.text()

		avatar_footer.delete_comment_from_avatar()
		avatar_footer = self.user_avatar.comments

		comment_after_delete = avatar_footer.last_comment.text()
		self.assertNotEqual(comment_before_delete, comment_after_delete)
