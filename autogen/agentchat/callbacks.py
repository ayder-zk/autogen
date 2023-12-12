from typing import Union, Dict, List, Optional

from autogen.agentchat.agent import Agent


class AgentCallbackHandler:

    def on_send(
            self,
            agent: Agent,
            message: Union[Dict, str],
            recipient: Agent,
            **kwargs
    ):
        """Run on the agent sends a message from the recipient."""

    async def on_a_send(
            self,
            agent: Agent,
            message: Union[Dict, str],
            recipient: Agent,
            **kwargs
    ):
        """
        (async) Run on the agent sends the message from the recipient.
        """

    def on_receive(
            self,
            agent: Agent,
            message: Union[Dict, str],
            sender: Agent,
            **kwargs):
        """Run on the agent receives the message from the sender."""

    async def on_a_receive(
            self,
            agent: Agent,
            message: Union[Dict, str],
            sender,
            **kwargs
    ):
        """
        (async) Run on the agent receives the message from the
        sender.
        """

    def on_generate_reply(
            self,
            agent: Agent,
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            **kwargs
    ):
        """Run on the agent generate reply."""

    async def on_a_generate_reply(
            self,
            agent: Agent,
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            **kwargs
    ):
        """(async) Run on the agent generates a reply."""

    async def on_llm_new_token(
            self,
            agent: Agent,
            token: str,
            sender: Optional[Agent] = None,
            **kwargs
    ):
        """
        (async) Run on new LLM token. Only available when streaming is
        enabled.
        """
