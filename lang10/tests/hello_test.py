import pytest
from assembly_client.api.contracts import ContractRef

@pytest.mark.usefixtures('network')
class TestHello():

    @pytest.fixture
    def reset_publish(self, network):
        network.upgrade_protocol(sympl_version=10)
        hello = ContractRef("hello", "1.0.0", 10)
        network.publish([hello])

    @pytest.fixture
    def key_alias(self, network):
        return network.register_key_alias()

    @pytest.fixture
    def hello(self, network, reset_publish, key_alias):
        return network[key_alias].hello["10-1.0.0"]

    def test_text_returned_from_hello_world(self, hello):
        assert hello.hello_world() == "Hello world!"
