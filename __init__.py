# Copyright 2017 Mycroft AI, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ovos_workshop.skills.fallback import FallbackSkill
import requests
import json


class FallbackCakeChatSkill(FallbackSkill):

    def initialize(self):
        self.register_fallback(self.handle_fallback_cakechat, 80)

    def handle_fallback_cakechat(self, message):
        header_content = {'Content-type': 'application/json'}
        utterance = message.data.get('utterance').lower()
        message = [utterance]
        js_data = json.dumps({'context': message, 'emotion': 'neutral'})
        host = self.settings.get("host", "http://0.0.0.0:8080")
        read_url = f'{host}/cakechat_api/v1/actions/get_response'
        response = requests.post(read_url,
                                 data=js_data,
                                 headers=header_content,
                                 verify=False)
        json_data = json.loads(response.text)
        self.speak(json_data["response"])
        return True
